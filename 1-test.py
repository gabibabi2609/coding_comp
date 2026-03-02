import sys
import time
import math

# Read number of test cases from stdin.
Test_line = sys.stdin.readline().rstrip()

T = int(Test_line)
print("Number of test cases:", T)
line = sys.stdin.readline().rstrip()

for i in range(T):
    a, b = map(int, line.split())
    total = a + b
    product = a * b
    print(total, product)
