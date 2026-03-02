# good practice to always import these:
import sys
import math
import string

# In competitive programming, input comes from standard input (stdin),
# not from interactive prompts like we've been doing in class.

# map() applies a function to each item in an iterable.
# split() separates a single string by whitespace, so you can use each part separately.

numbers = ["2", "5", "7"]
print("Original numbers as strings:", numbers)

# Use map() as a quick way to iterate the list and convert strings to numbers: 
# map() takes 2 arguement to apply int to each string in the list.

result = map(int, numbers)
print("Map result", result)

converted = list(result)
print("Converted object:", converted)

print("\n--- Using standard input ---")
#Read from standard input line by line.
#readline()
#rstrip() removed unwanted special characters
# Example expected input line:
# 3 7

line = sys.stdin.readline().rstrip()
print("Line:", line)

split_line = line.split() # by default it uses empty spaces to make the split
print("After split():", split_line)

a, b = map(int, split_line)

print("a =", a)
print("b =", b)

print("EXAMPLE ON HOW TO LOOP OVER MULTIPLE LINES AND MAP AND SPLIT THEM")
print()
# First, iterate over every line in standard input until End of File (EOF).
for l in sys.stdin:
    line = l.rstrip()

# Split the line into tokens and convert them to integers. REMEMBER: stdin defaults to strings so we neet to convert them to integers
    a, b = map(int, line.split())

    # compute the total of both numbers added together 
    total = a + b
    product = a * b
    # compute the product of both numbers
    # make sure they are only separated by a space
    print(total, product)


