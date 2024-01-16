command = input()
while command!= "End":
    if command == "SoftUni":
        command = input()
    for current_character in range (len(command)):
        print (command[current_character] * 2, end = "")
    print ()
    command = input()