# Drinking with Aaron.
## Video Demo:  <URL https://www.youtube.com/watch?v=3J92HELXkDU>
### Description:

I have chosen to make the world a better place by making a drinking card game. 

This game is run via a website, using HTML, CSS, JS, PYTHON, FLASK & SQLite3, just needing to "flask run" from the terminal to get started with everything downloaded and ready.

This is a cardgame - the aim of the game is to guess correctly four times in a row, each card offering different options. The first card offers red or black,
the second card offers higher or lower than the last card, the third card offers inside or outside the two cards on the table witht the fourth card offering, red or black or 
(compared to the last card) higher or lower. There is a full explanation in the how to play section. After the game has been completed, if you won you can post your score 
to the leaderboard. 

As this is a drinking game, for each wrong answer a sip is added to the tally and this should be paid at the end of the game, guess all options correctly with no 
mistakes and you can nominate a friend to finish thier drink. 

#### How different languages are used.

##### HTML & CSS
These are both used to make the website visible to its users, JS is also used to dynamically update innerHTML and visitiblity of divs as the game plays. 
Media Queries are used to make sure the game will work and look proper accross computers and mobile devies. 

##### JS
JS is used to run the game client side. JS holds everything related to the game - the rules, deck, cards, all functions to make the game work using recursion 
with correct boundries to avoid anything crashing. 

##### PYTHON
PYTHON is used with FLASK to check for GET & POST request, retrieve data from the website to later hold in SQLite3.
Using GET & POST requests PYHTON also makes sure the correct static files are loaded.
PYTHON will also query the database and pass back saved data to load the leaderboard when visiting /leaderboard.

##### JINJA 
JINJA is used to help populate the table to be visible to the users, iterating through the data passed from PYTHON into FLASK.

##### SQLite3
SQLite3 holds the data for the leaderboard, taking note of the users name, cards used and sips drunk. 

#### The files.

##### Static files.
These files hold the CSS and the JS script wihtout these i would have a very boring and non functional website. 

##### Templates.
These files hold the HTML for each of the webpages.

##### Application.py
Holds the flask structure, being able to use GET & POST request properly and using the data from SQLite3 properly. 

##### Leaderboard.db
Is the databse which holds the leaderboard. Data can be added and retrieved.


