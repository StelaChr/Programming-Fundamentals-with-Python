number_of_strings = int(input())

for current_string in range (number_of_strings):
    string = input()
    for current_character in range (len(string)):
        if string [current_character]  == "," or string [current_character]  == "." or string [current_character]  == "_":
            print (f"{string} is not pure!")
            break
    else:
        print (f"{string} is pure.")
