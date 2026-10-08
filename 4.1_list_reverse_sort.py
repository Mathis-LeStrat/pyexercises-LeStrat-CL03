"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: my list of 8 monthly budgets from exercise 4.0
# 2. Process: I make four reordered versions, always working on copies
# 3. Out: four orders, then the original list to prove it did not move
# 4. My four orders, and which ones modify the original:
#    - smallest to biggest with .sort(): .sort() MODIFIES the list in place,
#      so I use it on a copy made with .copy(), not on the original
#    - biggest to smallest with sorted(reverse=True): returns a NEW list
#    - August to January with [::-1]: slicing returns a NEW list
#    - starting from May with [4:] + [:4]: slicing returns a NEW list
#    .reverse() would also modify in place, so I did not use it.
#    Result: none of my four orders touches the original.


# Your code below

# Same list as in exercise 4.0
budgets = [1200, 950, 1500, 800, 1100, 1700, 900, 1300]

# Order 1: copy the list first, then sort the copy in place
ascending = budgets.copy()
ascending.sort()
print("Smallest to biggest:", ascending)

# Order 2: sorted() gives back a new list, biggest first
descending = sorted(budgets, reverse=True)
print("Biggest to smallest:", descending)

# Order 3: [::-1] reads the list backwards and makes a new list
backwards = budgets[::-1]
print("August to January:", backwards)

# Order 4: take May to August, then add January to April after
from_may = budgets[4:] + budgets[:4]
print("Starting from May:", from_may)

# Last line: show the original to prove it has not changed
print("Original list:", budgets)