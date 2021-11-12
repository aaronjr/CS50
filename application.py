import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    count = db.execute("SELECT symbol, price, name, sum(total_shares) AS shares from shares WHERE username = ? GROUP BY symbol", session["user_id"])
    cash = db.execute("SELECT cash from users WHERE id = ?", session["user_id"])

    for symbol in count:
        query = lookup(symbol["symbol"])
        symbol["price"] = query["price"]

    return render_template("index.html", counts = count, cash = cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        if lookup(symbol) == None:
            return apology("No share found", 400)
        if shares < 1:
            return apology("Shares requested must be greater than 0", 400)

        quote = lookup(symbol)
        CASH = db.execute("SELECT cash from users WHERE id = ?", session["user_id"])
        #get cash value
        cash = CASH[0]["cash"]
        #time
        date = datetime.datetime.now()
        now = date.strftime("%c")
        #empty list to compare to
        empty = []
        checkstock = db.execute("SELECT symbol from shares where username = ? and symbol = ? GROUP BY symbol", session["user_id"], quote["symbol"])

        if cash - (shares * quote["price"]) < 0:
            return apology("Not enough money", 400)

        elif checkstock == empty:
            cost = shares * quote["price"]
            left = cash - cost
            db.execute("UPDATE users SET cash = ? WHERE id = ?", left, session["user_id"])
            db.execute("INSERT INTO shares (username, symbol, name, price, total_shares, time) VALUES(?,?,?,?,?,?)",session["user_id"], quote["symbol"], quote["name"], quote["price"], shares, now)
            db.execute("INSERT INTO history (username, symbol, name, price, total_shares, time, type) VALUES(?,?,?,?,?,?,?)",session["user_id"], quote["symbol"], quote["name"], quote["price"], shares, now, "bought")
            return redirect("/")

        elif quote["symbol"] == checkstock[0]["symbol"]:
            cost = shares * quote["price"]
            left = cash - cost
            currentshares = db.execute("SELECT total_shares from shares where username = ? and symbol = ? GROUP BY symbol", session["user_id"], quote["symbol"])
            newshares = currentshares[0]["total_shares"] + shares
            db.execute("UPDATE shares SET total_shares = ? WHERE username = ? and symbol = ?", newshares, session["user_id"], quote["symbol"])
            db.execute("UPDATE users SET cash = ? WHERE id = ?", left, session["user_id"])
            db.execute("INSERT INTO history (username, symbol, name, price, total_shares, time, type) VALUES(?,?,?,?,?,?,?)",session["user_id"], quote["symbol"], quote["name"], quote["price"], shares, now, "bought")
            return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    count = db.execute("SELECT symbol, price, name, time, type, total_shares as shares from history WHERE username = ?", session["user_id"])
    cash = db.execute("SELECT cash from users WHERE id = ?", session["user_id"])
    sold = "sold"

    return render_template("history.html", counts = count, cash = cash, sold = sold)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if lookup(symbol) == None:
            return apology("No share found", 403)
        return render_template("quoted.html", quote = lookup(symbol))

    if request.method == "GET":
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
         # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

         # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure passwords match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("Passwords do not match", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        username = request.form.get("username")
        password = request.form.get("password")
        # Ensure username does not exist
        if len(rows) >= 1:
           return apology("Username already exists", 400)

        else:
            db.execute("INSERT INTO users (username, hash) VALUES(?,?)", username, generate_password_hash(password, method='pbkdf2:sha256', salt_length=8))
            sessions = db.execute("SELECT id from users where username = ?", username)
            session["user_id"] = sessions[0]["id"]
            return redirect("/")

    if request.method == "GET":
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":

        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        quote = lookup(symbol)
        
        if shares < 1:
            return apology("Shares to sell must be greater than 0", 403)

        checksymbol = db.execute("SELECT symbol, total_shares from shares WHERE symbol = ? and username = ?", symbol, session["user_id"])

         #time
        date = datetime.datetime.now()
        now = date.strftime("%c")

        CASH = db.execute("SELECT cash from users WHERE id = ?", session["user_id"])
        #get cash value
        cash = CASH[0]["cash"]

        if shares == 0:
            return apology("Must chose more than 0 shares to sell", 400)

        elif checksymbol[0]["total_shares"] == shares:
            cost = shares * quote["price"]
            left = cash + cost
            db.execute("UPDATE users SET cash = ? WHERE id = ?", left, session["user_id"])
            db.execute("DELETE from shares where username = ? and symbol = ?", session["user_id"], symbol)
            db.execute("INSERT INTO history (username, symbol, name, price, total_shares, time, type) VALUES(?,?,?,?,?,?,?)",session["user_id"], quote["symbol"], quote["name"], quote["price"], shares, now, "sold")

        elif symbol == checksymbol[0]["symbol"] and shares <= checksymbol[0]["total_shares"]:
            newshares = checksymbol[0]["total_shares"] - shares
            cost = shares * quote["price"]
            left = cash + cost
            db.execute("UPDATE users SET cash = ? WHERE id = ?", left, session["user_id"])
            db.execute("UPDATE shares SET total_shares = ? WHERE username = ? and symbol = ?", newshares, session["user_id"], quote["symbol"])
            db.execute("INSERT INTO history (username, symbol, name, price, total_shares, time, type) VALUES(?,?,?,?,?,?,?)",session["user_id"], quote["symbol"], quote["name"], quote["price"], shares, now, "sold")

        else:
             return apology("You do not have enough shares", 400)


        return redirect("/")

    if request.method == "GET":

        symbol = db.execute("SELECT symbol from shares WHERE username = ? GROUP BY symbol", session["user_id"])
        return render_template("sell.html", symbols = symbol)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
