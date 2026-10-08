"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the user's answer to "Do you approve the campaign budget?"
# 2. Process: I keep asking until the answer is "yes" or until 3 attempts are used.
#    Before comparing, I clean the answer with strip() and lower(),
#    so "Yes", "yes" and " YES " all count as yes.
# 3. Out: a summary with the number of attempts, the answers typed and the result
# 4. My stop condition, my attempt limit, my summary:
#    Stop condition: the user answers yes.
#    Limit: 3 attempts maximum, then the program stops with "no approval".
#    Summary: attempts used, the list of answers, and approved or not.


# Your code below

# Settings and counters before the loop
max_attempts = 3
attempts = 0
answers = []
approved = False

# Keep asking while the limit is not reached and the budget is not approved
while attempts < max_attempts and not approved:
    answer = input("Do you approve the campaign budget? (yes/no): ")
    attempts = attempts + 1
    answers.append(answer)
    # Clean the answer: remove the spaces and put it in lowercase
    if answer.strip().lower() == "yes":
        approved = True

# Show the summary of what happened in the loop
print("--- Summary ---")
print("Attempts used:", attempts, "out of", max_attempts)
print("Answers typed:", answers)
if approved:
    print("Result: budget approved.")
else:
    print("Result: no approval after", max_attempts, "attempts, the program stops.")