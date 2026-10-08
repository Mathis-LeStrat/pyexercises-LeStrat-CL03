"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: my list of 8 monthly budgets from exercise 4.0
# 2. Process: for each budget, I take its position (the month number)
#    and compute its share of the total budget in percent
# 3. Out: one line per month with the month number, the budget and its share
# 4. What I compute for each item, and why it is worth showing:
#    The share of the total. The reader sees at once which month took
#    the biggest part of the money (month 6, 18%) and which took the least.


# Your code below

# Same list as in exercise 4.0, monthly budgets from January to August
budgets = [1200, 950, 1500, 800, 1100, 1700, 900, 1300]

# Total of all budgets, needed to compute each share
total = sum(budgets)

# For each budget, enumerate gives its position, starting at 1 for January.
# Then I compute its share of the total, rounded to 1 decimal.
for position, budget in enumerate(budgets, start=1):
    share = round(budget / total * 100, 1)
    print("Month", position, ":", budget, "euros, which is", share, "% of the total")