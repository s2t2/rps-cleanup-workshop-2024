# the "app/rps.py" file (v1)...

from random import choice

VALID_OPTIONS = ["rock", "paper", "scissors"]

#
# USER SELECTION
#

u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
print("USER CHOICE:", u)
if u not in VALID_OPTIONS:
    print("OOPS, TRY AGAIN")
    exit()

#
# COMPUTER SELECTION
#

c = choice(VALID_OPTIONS)
print("COMPUTER CHOICE:", c)

#
# DETERMINATION OF WINNER
#

def determine_outcome(u:str, c:str):
    """Determines the winner in a game of R, P, S.

    Params :
        u (str): user choice - one of the valid options ("rock", "paper", "scissors")
        c (str): computer choice - one of the valid options ("rock", "paper", "scissors")
    """

    if u == "rock" and c == "rock":
        return "TIE GAME"
    elif u == "rock" and c == "paper":
        return "COMPUTER WINS"
    elif u == "rock" and c == "scissors":
        return "USER WINS"
    elif u == "paper" and c == "rock":
        return "USER WINS"
    elif u == "paper" and c == "paper":
        return "TIE GAME"
    elif u == "paper" and c == "scissors":
        return "COMPUTER WINS"
    elif u == "scissors" and c == "rock":
        return "COMPUTER WINS"
    elif u == "scissors" and c == "paper":
        return "USER WINS"
    elif u == "scissors" and c == "scissors":
        return "TIE GAME"


outcome = determine_outcome(u, c)
print(outcome)
