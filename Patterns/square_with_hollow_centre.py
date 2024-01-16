size_of_square = int(input())

for row in range (1,size_of_square+1 ):
    if row == 1 or row == size_of_square:
        print ("*"* size_of_square)
        continue
    print ("*" + (" "* (size_of_square- 2)) + "*" )

