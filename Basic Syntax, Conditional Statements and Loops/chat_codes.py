number_of_messages = int(input())
message = ""

for current_message in range (number_of_messages):
    number = int(input())
    if number == 88:
        message = "Hello"
    elif number == 86:
        message = "How are you?"
    elif number < 88:
        message =  "GREAT!"
    elif number > 88:
        message = "Bye."
    print (message)
