"""Exercise 2.0 — Asking the user

WHAT THE PROGRAM MUST DO
    Ask the user for two pieces of information, then display a sentence that uses both.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two pieces of information did you choose, and for what purpose?
       Imagine a real form in your future job. Not "name and age" unless you can
       say what you would do with them.

WHAT THE AI CANNOT KNOW
    Your two fields, and the sentence you want at the end. Decide both before you ask.

    One of your two values will almost certainly need to be a number. Find out what
    happens when you try to add 1 to something the user typed, and deal with it.

CHECK IT YOURSELF
    Run your program and answer with an empty line. Then with a space. Then with text
    where you expected a number. Write in a comment what happened each time.
    You are not asked to fix it yet, only to see it.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the name of a person signing up, and the number of guests they bring (typed as text).
# 2. Process: the number of guests is converted from text to a whole number with int(),
#    then 1 is added to count the person themself, so we get the total seats to book.
# 3. Out: a confirmation sentence with the person's name and the number of seats reserved.
# 4. My two fields, and what I would do with them:
#    A registration form for a company event (afterwork, seminar). The name is used to
#    greet the person and put them on the guest list; the number of guests is used to
#    know how many seats and meals to order from the caterer.


# Your code below

# Ask for the name of the person who registers (input always gives back text)
name = input("Your name: ")

# Ask how many guests they bring, and turn the text into a number with int(),
# otherwise "2" + 1 crashes with a TypeError (you cannot add text and a number)
guests = int(input("Number of guests you bring: "))

# Add the person themself to their guests to get the seats to reserve
seats = guests + 1

# Show the confirmation sentence that uses both pieces of information
print(f"Thank you {name}, {seats} seat(s) are reserved for you and your guests.")


# CHECK IT YOURSELF
# Normal run: name "Mathis", guests "2"
#   -> "Thank you Mathis, 3 seat(s) are reserved for you and your guests."  As expected.
# Before adding int(): guests + 1 gave
#   TypeError: can only concatenate str (not "int") to str
#   because input() returns the text "2", not the number 2.
# Empty line for the name: no error, it prints "Thank you , 3 seat(s)..." with a blank name.
# A space for the name: no error either, it prints "Thank you  , 3 seat(s)..." (looks empty).
# Empty line for the guests: crash,
#   ValueError: invalid literal for int() with base 10: ''
# A space for the guests: crash, ValueError: invalid literal for int() with base 10: ' '
# Text instead of a number ("two"): crash,
#   ValueError: invalid literal for int() with base 10: 'two'
# Conclusion: the name accepts anything, even nothing; the number crashes on anything
# that is not digits. Not fixed yet, as the brief asks.
