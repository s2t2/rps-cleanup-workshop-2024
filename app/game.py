# the "app/rps.py" file (v1)...

from random import choice

VALID_OPTIONS = ["rock", "paper", "scissors"]


def generate_computer_choice():
    return choice(VALID_OPTIONS)

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


if __name__ == "__main__":
    # only run the contents below when we run this file from the command line
    # but not when we import content from this file

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

    c = generate_computer_choice()
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #

    outcome = determine_outcome(u, c)
    print(outcome)
