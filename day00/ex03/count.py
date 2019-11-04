import sys
import string
from collections import Counter


def text_analyzer(text=""):
    """    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""
    if text:
        c = Counter("upper" if x.isupper() else "lower" if x.islower()
                    else "space" if x.isspace()
                    else "punctuation" if x in string.punctuation
                    else "other" for x in text)
        nb_char = sum(list(c.values()))
        print("The text contains " + str(nb_char) + " characters:")
        print("- " + str(c["upper"]) + " upper letters")
        print("- " + str(c["lower"]) + " lower letters")
        print("- " + str(c["punctuation"]) + " punctuation marks")
        print("- " + str(c["space"]) + " spaces")
    else:
        text = input("What is the text to analyse?\n>> ")
        text_analyzer(text)
