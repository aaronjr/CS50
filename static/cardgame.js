var data = {}

function startGame() {

    // Create a deck
    let suits = ["♥", "♦", "♠", "♣"];
    let value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13];
    let face = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"];
    let word = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"];
    let deck = [];
    var todrink = 0;
    var n = 0;
    
    // loop through all suits and cards = 52 cards
    // loop through 4 suits
    for (let i = 0; i < 4; i++) {
        // loop through 13 cards
        for (let j = 0; j < 13; j++) {
            // make a card
            card = {};
            card['suit'] = suits[i];
            suits[i] == "♥" || suits[i] == "♦" ? card['color'] = "red" : card['color'] = "black";
            card['value'] = value[j];
            card['face'] = face[j];
            card['word'] = word[j];
            // add card to deck
            deck.push(card);
        }
    }

    // Global variables
    let currentCard = [];
    let lastCard = [];
    let otherCard = [];

    // cards from HTML
    const card1 = document.getElementById("card1");
    const card2 = document.getElementById("card2");
    const card3 = document.getElementById("card3");
    const card4 = document.getElementById("card4");
    // boxes from HTML
    const box1 = document.getElementById("box1");
    const box2 = document.getElementById("box2");
    const box3 = document.getElementById("box3");
    const box4 = document.getElementById("box4");
    const box5 = document.getElementById("box5");
    const box6 = document.getElementById("box6");


    function newCard() {
        // make a new card - find random card and remove from deck, return as current card
        n = deck.length - 1;
        number = Math.floor(Math.random() * n + 1);
        currentCard = deck[number];
        deck.splice(number, 1);
        return currentCard;
    }

    function clearup() {
        // reset all boxes to first option - red or black
        document.getElementById("text").innerHTML = "Red or Black?";
        document.getElementById("box2").innerHTML = "Red";
        document.getElementById("box3").innerHTML = "Black";

        document.getElementById("card1").innerHTML = "";
        document.getElementById("card2").innerHTML = "";
        document.getElementById("card3").innerHTML = "";
        document.getElementById("card4").innerHTML = "";

        card1.setAttribute("data-value", "");
        card2.setAttribute("data-value", "");
        card3.setAttribute("data-value", "");
        card4.setAttribute("data-value", "");

        card1.classList.add("checkered45");
        card2.classList.add("checkered45");
        card3.classList.add("checkered45");
        card4.classList.add("checkered45");

        box1.style.visibility = 'hidden';
        box2.style.visibility = 'visible';
        box3.style.visibility = 'visible';
        box4.style.visibility = 'hidden';
        box5.style.display = 'none';
        box6.style.display = 'none';
    }

    function nopairs() {
        // text for no pairs in this game
        document.getElementById("text").innerHTML = "No pairs in this game!!";
    }

    function emptybox() {
        // hide all boxes
        box1.style.visibility = 'hidden';
        box2.style.visibility = 'hidden';
        box3.style.visibility = 'hidden';
        box4.style.visibility = 'hidden';
    }

    function cardOne() {
        // dynamic changes for card 1 
        card1.classList.remove("checkered45");
        document.getElementById("card1").innerHTML = currentCard["face"] + currentCard["suit"];
        currentCard["suit"] == "♥" || currentCard["suit"] == "♦" ? card1.style.color = "red" : card1.style.color = "black";
        card1.setAttribute("data-value", currentCard["face"] + currentCard["suit"]);
    }

    function cardTwo() {
        // dynamic changes for card 2
        card2.classList.remove("checkered45");
        document.getElementById("card2").innerHTML = currentCard["face"] + currentCard["suit"];
        currentCard["suit"] == "♥" || currentCard["suit"] == "♦" ? card2.style.color = "red" : card2.style.color = "black";
        card2.setAttribute("data-value", currentCard["face"] + currentCard["suit"]);
    }

    function cardThree() {
        // dynamic changes for card 3
        card3.classList.remove("checkered45");
        document.getElementById("card3").innerHTML = currentCard["face"] + currentCard["suit"];
        currentCard["suit"] == "♥" || currentCard["suit"] == "♦" ? card3.style.color = "red" : card3.style.color = "black";
        card3.setAttribute("data-value", currentCard["face"] + currentCard["suit"]);

    }

    function cardFour() {
        // dynamic changes for card 4
        card4.classList.remove("checkered45");
        document.getElementById("card4").innerHTML = currentCard["face"] + currentCard["suit"];
        currentCard["suit"] == "♥" || currentCard["suit"] == "♦" ? card4.style.color = "red" : card4.style.color = "black";
        card4.setAttribute("data-value", currentCard["face"] + currentCard["suit"]);
    }


    function red_black() {
        //get new card, prompt for choice then compare values
        clearup();
        newCard();
        // drinks and cards remaining at top of the game - repeated throughout. 
        document.getElementById("remain").innerHTML = "Cards remaining: " + n;
        document.getElementById("drink").innerHTML = "To drink: " + todrink;
        // below is the hidden boxes being updated to pull through flask into python for leaderboard
        document.getElementById("todrink").value = todrink;
        document.getElementById("n").value = n;
        clearup();
        
        // add to drinks counter after each wrong answer
        todrink++;
        
        //check user not out of cards
        if (n < 4) {
            outofcards()
        }

        window.onclick = e => {
            // check for input check if correct, if correct next option if not reload red or black
            if (e.target.innerHTML == "Red") {
                if (currentCard["color"] == "red") {
                    cardOne()
                    lastCard = currentCard;
                    emptybox();
                    higher_lower()
                } else {
                    //recall red or black
                    cardOne()
                    document.getElementById("text").innerHTML =
                        "WRONG!! " + currentCard["face"] + currentCard["suit"] +
                        " is not red!";
                    emptybox();
                    setTimeout(red_black, 1500)

                }

            }
            // check for input check if correct, if correct next option if not reload red or black
            if (e.target.innerHTML == "Black") {
                if (currentCard["color"] == "black") {
                    cardOne()
                    lastCard = currentCard;
                    emptybox();
                    higher_lower()
                } else {
                    //recall red or black
                    cardOne()
                    document.getElementById("text").innerHTML =
                        "WRONG!! " + currentCard["face"] + currentCard["suit"] +
                        " is not black!";
                    emptybox();
                    setTimeout(red_black, 1500)


                }
            }
        };
    }

    function higher_lower() {

        newCard();

        document.getElementById("remain").innerHTML = "Cards remaining: " + n;
        document.getElementById("n").value = n;

        box2.style.visibility = 'visible';
        box3.style.visibility = 'visible';
        document.getElementById("text").innerHTML = "Higher or lower than " + lastCard["word"] + "?";
        document.getElementById("box2").innerHTML = "Higher";
        document.getElementById("box3").innerHTML = "Lower";


        window.onclick = e => {
            // check for input check if correct, if correct next option if not reload red or black
            if (e.target.innerHTML == "Higher") {
                if (currentCard["value"] > lastCard["value"]) {
                    cardTwo()
                    otherCard = lastCard;
                    lastCard = currentCard;
                    emptybox();
                    inside_outside();
                } else {
                    cardTwo()
                    if (currentCard["value"] != lastCard["value"]) {
                        document.getElementById("text").innerHTML =
                            "WRONG!! " + currentCard["face"] + " is not higher than a " +
                            lastCard["face"] + "!";
                    } else {
                        nopairs();
                    }
                    emptybox();
                    setTimeout(red_black, 1500);
                }
            }
            
            // check for input check if correct, if correct next option if not reload red or black
            if (e.target.innerHTML == "Lower") {
                if (currentCard["value"] < lastCard["value"]) {
                    cardTwo()
                    otherCard = lastCard;
                    lastCard = currentCard;
                    emptybox();
                    inside_outside();
                } else {
                    //recall red or black
                    cardTwo()
                    if (currentCard["value"] != lastCard["value"]) {
                        document.getElementById("text").innerHTML = "WRONG!! " + currentCard["face"] + " is not lower than a " +
                            lastCard["face"] + "!";
                    } else {
                        nopairs();
                    }
                    emptybox();
                    setTimeout(red_black, 1500);
                }
            }
        };
    }

    function inside_outside() {
        newCard();
        document.getElementById("remain").innerHTML = "Cards remaining: " + n;
        document.getElementById("n").value = n;

        box2.style.visibility = 'visible';
        box3.style.visibility = 'visible';
        document.getElementById("text").innerHTML = "Inside or outside of " + otherCard["word"] + " and " + lastCard["word"] + "?";
        document.getElementById("box2").innerHTML = "Inside";
        document.getElementById("box3").innerHTML = "Outside";

        window.onclick = e => {
            // check for input check if correct, if correct next option if not reload red or black
            if (e.target.innerHTML == "Inside") {
                if (currentCard["value"] > lastCard["value"] && currentCard["value"] < otherCard["value"] || currentCard[
                        "value"] < lastCard["value"] && currentCard["value"] > otherCard["value"]) {
                    cardThree()
                    lastCard = currentCard;
                    emptybox();
                    allfour();
                } else {
                    //recall red or black
                    cardThree()
                    if (currentCard["value"] != lastCard["value"] && currentCard["value"] != otherCard["value"]) {
                        document.getElementById("text").innerHTML = "WRONG!! " + currentCard["face"] + " is not inbetween of " +
                            lastCard["face"] + " and " + otherCard["face"] + "!";
                    } else {
                        nopairs();
                    }
                    emptybox();
                    setTimeout(red_black, 1500)
                }

            }
            // check for input check if correct, if correct next option if not reload red or black
            if (e.target.innerHTML == "Outside") {
                if (currentCard["value"] < lastCard["value"] && currentCard["value"] < otherCard["value"] || currentCard[
                        "value"] > lastCard["value"] && currentCard["value"] > otherCard["value"]) {
                    cardThree()
                    lastCard = currentCard;
                    emptybox();
                    allfour();
                } else {
                    //recall red or black
                    cardThree()
                    if (currentCard["value"] != lastCard["value"] && currentCard["value"] != otherCard["value"]) {
                        document.getElementById("text").innerHTML = "WRONG!! " + currentCard["face"] + " is not outside of " +
                            lastCard["face"] + " and " + otherCard["face"] + "!";
                    } else {
                        nopairs();
                    }
                    emptybox();
                    setTimeout(red_black, 1500)
                }
            }
        };
    }

    function allfour() {
        newCard();
        document.getElementById("remain").innerHTML = "Cards remaining: " + n;
        document.getElementById("n").value = n;

        text.style.fontSize = "2.5rem";
        box1.style.visibility = 'visible';
        box2.style.visibility = 'visible';
        box3.style.visibility = 'visible';
        box4.style.visibility = 'visible';

        document.getElementById("text").innerHTML = "Is the next card red or black or is it higher or lower than the " + lastCard[
            "word"] + "?";
        document.getElementById("box1").innerHTML = "Red";
        document.getElementById("box2").innerHTML = "Black";
        document.getElementById("box3").innerHTML = "Higher";
        document.getElementById("box4").innerHTML = "Lower";

        window.onclick = e => {
            // check for input check if correct, if correct next option if not reload red or black
            if (e.target.innerHTML == "Red") {
                if (currentCard["color"] == "red") {
                    if (currentCard["value"] == lastCard["value"]) {
                        cardFour();
                        nopairs();
                        emptybox();
                        setTimeout(red_black, 1500)
                    } else {
                        cardFour()
                        document.getElementById("text").innerHTML = "WINNER!!";
                        addToLeaderboard()
                    }
                } else {
                    //recall red or black
                    cardFour()
                    if (currentCard["value"] != lastCard["value"]) {
                        document.getElementById("text").innerHTML = "WRONG!! " + currentCard["face"] + currentCard["suit"] +
                            " is not red!";
                    } else {
                        nopairs();
                    }
                    emptybox();
                    setTimeout(red_black, 1500)
                }
            } // check for input check if correct, if correct next option if not reload red or black
            else if (e.target.innerHTML == "Black") {
                if (currentCard["color"] == "black") {
                    if (currentCard["value"] == lastCard["value"]) {
                        cardFour()
                        nopairs();
                        emptybox();
                        setTimeout(red_black, 1500)
                    } else {
                        card4.classList.remove("checkered45");
                        document.getElementById("card4").innerHTML = currentCard["face"] + currentCard["suit"];
                        currentCard["suit"] == "♥" || currentCard["suit"] == "♦" ? card4.style.color = "red" : card4.style
                            .color = "black";
                        card4.setAttribute("data-value", currentCard["face"] + currentCard["suit"]);
                        addToLeaderboard()
                    }
                } else {
                    //recall red or black
                    cardFour()
                    if (currentCard["value"] != lastCard["value"]) {
                        document.getElementById("text").innerHTML = "WRONG!! " + currentCard["face"] + currentCard["suit"] +
                            " is not black!";
                    } else {
                        nopairs();
                    }
                    emptybox();
                    setTimeout(red_black, 1500);
                }
            } // check for input check if correct, if correct next option if not reload red or black
            else if (e.target.innerHTML == "Higher") {
                if (currentCard["value"] > lastCard["value"]) {
                    if (currentCard["value"] == lastCard["value"]) {
                        cardFour()
                        nopairs();
                        emptybox();
                        setTimeout(red_black, 1500)
                    } else {
                        cardFour()
                        document.getElementById("text").innerHTML = "WINNER!!";
                        addToLeaderboard()
                    }
                } else {
                    cardFour()
                    if (currentCard["value"] != lastCard["value"]) {
                        document.getElementById("text").innerHTML = "WRONG!! " + currentCard["face"] + " is not higher than a "
                            + lastCard["face"] + "!";
                    } else {
                        nopairs();
                    }
                    emptybox();
                    setTimeout(red_black, 1500)
                }
            } // check for input check if correct, if correct next option if not reload red or black
            else if (e.target.innerHTML == "Lower") {
                if (currentCard["value"] < lastCard["value"]) {
                    if (currentCard["value"] == lastCard["value"]) {
                        cardFour()
                        nopairs();
                        emptybox();
                        setTimeout(red_black, 1500)
                    } else {
                        cardFour()
                        document.getElementById("text").innerHTML = "WINNER!!";
                        addToLeaderboard()
                    }
                } else {
                    //recall red or black
                    cardFour()
                    if (currentCard["value"] != lastCard["value"]) {
                        document.getElementById("text").innerHTML = "WRONG!! " + currentCard["face"] +
                            " is not lower than a " + lastCard["face"] + "!";
                    } else {
                        nopairs();
                    }
                    emptybox();
                    setTimeout(red_black, 1500)
                }
            }
        };

    }
    
    // if out of cards, hide boxes and offer to play again
    function outofcards() {
        box1.style.visibility = 'hidden';
        box2.style.visibility = 'hidden';
        box3.style.visibility = 'hidden';
        box4.style.visibility = 'hidden';
        document.getElementById("text").innerHTML = "Out of cards!!";
        setTimeout(playagain, 1500)
    }
    
    // offer user to play again.
    function playagain() {
        //hid not needed boxes
        text.style.fontSize = "4rem";
        box1.style.visibility = 'hidden';
        box2.style.visibility = 'visible';
        box3.style.visibility = 'visible';
        box4.style.visibility = 'hidden';
    
        // checking for a perfect game
        if (todrink == 1) {
            drink.style.fontSize = "1.5rem";
            document.getElementById("drink").innerHTML = "Nominate someone to finish their drink!";
            remain.style.fontSize = "2rem";
            document.getElementById("remain").innerHTML = "Did it in one!";
        }
        
        // offer to play again
        document.getElementById("text").innerHTML = "Play again?";
        document.getElementById("box2").innerHTML = "Yes";
        document.getElementById("box3").innerHTML = "No";
        
        // if user clicks yes, page will reload causing the first functions to be called
        // and the game will restart
        window.onclick = e => {
            if (e.target.innerHTML == "Yes") {
                window.location.reload();
            }
        }
        // if user clicks no, user redircted to landing page
        document.getElementById("box3").onclick = function() {
            location.href = "/";
        };

    }

    // add scores to leaderboard
    function addToLeaderboard() {
        
        // hide the boxes that arent needed
        text.style.fontSize = "4rem";
        box1.style.visibility = 'hidden';
        box4.style.visibility = 'hidden';
    
        // checking for perfect game
        if (todrink == 1) {
            drink.style.fontSize = "1.5rem";
            document.getElementById("drink").innerHTML = "Nominate someone to finish their drink!";
            remain.style.fontSize = "2rem";
            document.getElementById("remain").innerHTML = "Did it in one!";
        }
        
        // offer the chance to update leaderboard
        document.getElementById("text").innerHTML = "Update leaderboard?";
        document.getElementById("box2").innerHTML = "Yes";
        document.getElementById("box3").innerHTML = "No";
        
        // hide all other boxes, show input and submit box
        window.onclick = e => {
            if (e.target.innerHTML == "Yes") {
                box1.style.display = 'none';
                box2.style.display = 'none';
                box3.style.display = 'none';
                box4.style.display = 'none';
                box5.style.display = 'block';
                box6.style.display = 'block';
                box5.style.cursor = 'text';
            }
            // if user doesnt want to submit, offer play again
            if (e.target.innerHTML == "No") {
                playagain();

            }
        }


    }

    // function calls the first function needed recursion is used after and self controls. 
    red_black();

}

// JS page calls this function immeditalty. 
startGame()