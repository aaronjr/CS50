import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

# Configure application
app = Flask(__name__)

db = SQL("sqlite:///leaderboard.db")

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# homepage - with three options


@app.route("/", methods=["GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")

# the card game


@app.route("/cardgame", methods=["GET", "POST"])
def cardgame():
    # get loads game
    if request.method == "GET":
        return render_template("cardgame.html")
        
    # post takes data for leaderboard
    if request.method == "POST":
        
        # get three data entries needed, name, used cards and sips
        name = request.form.get("name")
        used = request.form.get("n") 
        sips = request.form.get("todrink") 
        
        # make the cards left instead of cards used
        left = 52 - int(used)
        
        print(int(left))
        
        # check for a perfect game
        if int(left) == 4:
            perfect = "Yes"
        else:
            perfect = "No"
        
        # add to DB
        db.execute("INSERT INTO leaderboard (name, left, sips, perfect) VALUES (?,?,?,?)",
                   name, left, sips, perfect)
        
        return redirect("/leaderboard")
       
        
# rules for the game       
@app.route("/howto", methods=["GET"])
def howto():
    if request.method == "GET":
        return render_template("howto.html")


# load leaderboard
@app.route("/leaderboard", methods=["GET"])
def leaderboard():
    # take data store in a variable and push to jinja
    if request.method == "GET":

        score = db.execute(
            "SELECT * from leaderboard ORDER BY cast(left as int) asc")

        return render_template("leaderboard.html", scores=score)

