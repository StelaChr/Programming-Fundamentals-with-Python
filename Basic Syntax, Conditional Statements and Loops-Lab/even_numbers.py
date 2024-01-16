qty_of_numbers = int(input())

for current_number in range (qty_of_numbers):
    number = int(input())
    if number %2!= 0:
        print (f"{number} is odd!" )
        break
else:
    print ("All numbers are even.")
