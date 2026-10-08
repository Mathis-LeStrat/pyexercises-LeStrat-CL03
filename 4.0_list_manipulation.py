"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a list of 8 monthly social media budgets in euros, January to August
# 2. Process: I pick one month, sort the budgets, and compute the total and the average
# 3. Out: the whole list, the March budget, the sorted list, the total and the average
# 4. What my list is about, and what I computed from it: #    My list is the monthly advertising budget of a brand on social media.
#    I computed the total spent and the average per month. The average is
#    interesting because it shows if a month is above or below normal spending.



# Your code below

budgets = [1200, 950, 1500, 800, 1100, 1700, 900, 1300]


print("All budgets:", budgets)


print("March budget:", budgets[2])


print("Sorted:", sorted(budgets))


total = sum(budgets)
print("Total:", total)
print("Average per month:", total / len(budgets))


print("First three total:", sum(budgets[:3]))