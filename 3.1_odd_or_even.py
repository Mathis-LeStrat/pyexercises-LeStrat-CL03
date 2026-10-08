"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a whole number N typed by the user
# 2. Process: for each number from 1 to N, I check the remainder of the division by 2 (% 2)
# 3. Out:one line per number saying "is odd" or "is even"
# 4. What happens on 0, on a negative number, on a very large number: #    0 or negative: a message asks for a number bigger than 0, because "from 1 to N" makes no sense.     Bigger than 100: a message says it is too big, nobody wants to read 5000 lines.



# Your code below
n = int(input("Type a number N: "))

if n <= 0:
    print("Please type a number bigger than 0.")

elif n > 100:
    print("Too big: please type a number up to 100.")

else:
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")