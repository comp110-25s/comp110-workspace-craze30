"""Creating Wordle!"""

__author__: str = "730567389"


def contains_char(string1: str, string2: str) -> bool:
    """Searches through a given string to find if a string character matches"""
    assert len(string2) == 1, f"len('{string2}) is not 1"
    idx: int = 0
    while idx < len(string1):
        if string2 == string1[idx]:
            return True
        idx += 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guessword: str, secword: str) -> str:
    """Evaluates guessed word on correctness"""
    assert len(guessword) == len(secword), "Guess must be same length as secret"
    output = ""
    idx: int = 0
    while idx < len(guessword):
        if guessword[idx] == secword[idx]:
            output += GREEN_BOX
        elif contains_char(string1=secword, string2=guessword[idx]):
            output += YELLOW_BOX
        else:
            output += WHITE_BOX
        idx += 1
    return output


def input_guess(explength: int) -> str:
    """Asks user how many characters in the word"""
    guess = input(f"Enter a {explength} character word")
    while len(guess) != explength:
        guess = input(f"That wasn't {explength} chars! Try again:")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turncount: int = 1
    wincondition: int = 0
    while turncount <= 6 and wincondition == 0:
        print(f" === Turn {turncount}/6 === ")
        guessword = input_guess(explength=len(secret))
        print(emojified(guessword, secword=secret))
        turncount += 1
        if guessword == secret:
            wincondition += 1

    if turncount >= 6:
        print("X/6 - Sorry, try again tomorrow!")

    else:
        print(f"You won in {turncount-1}/6 turns!")

    if __name__ == "__main__":
        main(secret="codes")
