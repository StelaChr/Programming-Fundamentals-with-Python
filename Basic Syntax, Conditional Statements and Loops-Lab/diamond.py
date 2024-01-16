from math import ceil
number = int(input())

for row in range (1, ceil(number/2) +2):
    if number % 2==0:
        if row == number/2 or row == number/2 + 1:
            print ("*" * number)
            continue
        print ((" " * (ceil(number/2) - row)) + ("*" * 2* row) + (" " * (ceil(number/2) - row)))
    else:
        if row ==ceil((number/2)):
            print("*" * number)
            continue
        print ((" " * (ceil(number / 2) - row)) + ("*" * 2* row) + (" " * (ceil(number / 2) - row)))

for row in range (ceil(number/2) - 1, 0, -1):
    print ((" " * (ceil(number/2) - row)) + ("*" * 2 * row) + (" " * (ceil(number/2) - row)))