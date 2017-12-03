import sys

spreadsheet = open('input1.txt')

total = 0
for line in spreadsheet:
    line = line.split()
    sm = float('inf')
    lg = float('-inf')
    for num in line:
        num = int(num)
        if num > lg:
            lg = num
        if num < sm:
            sm = num

    total += (lg-sm)

print total
