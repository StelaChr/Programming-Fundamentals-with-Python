number = int(input())
for row in range (1, number+1):
    for position_in_row in range (0, row):
        print ("*", end = "")
    print()