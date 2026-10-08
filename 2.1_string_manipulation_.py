"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: one sentence typed by the user (text, possibly with extra spaces and mixed capitals).
# 2. Process: the same sentence goes through four string methods, each giving a new version.
#    The original sentence is never changed, because strings in Python cannot be modified.
# 3. Out: four lines, each showing one transformed version of the sentence.
# 4. My four transformations, and when each is useful:
#    - strip(): clean a value typed in a form before saving it (no invisible spaces in a database).
#    - upper(): write a name or code in capitals, like a surname on an official document or a badge.
#    - title(): turn a title or product name into a clean heading, capital on each word.
#    - lower() + replace(" ", "_"): build a file name or URL from a sentence (no spaces, no capitals).


# Your code below

# Ask the user for a sentence (kept exactly as typed, spaces included)
sentence = input("Type a sentence: ")

# 1. Remove the spaces at the start and the end; repr() shows the quotes so we can see them
print("strip()  :", repr(sentence.strip()))

# 2. Put everything in capitals, without cleaning first, to see that spaces are kept
print("upper()  :", repr(sentence.upper()))

# 3. Clean the ends, then give each word a capital first letter
print("title()  :", repr(sentence.strip().title()))

# 4. Clean the ends, put everything in lowercase, then replace spaces with "_" to get a file name
print("file name:", repr(sentence.strip().lower().replace(" ", "_")))
