first_string = input()
second_string = input()
last_word = first_string

for character_index in range (len(first_string)):
    left_part = second_string [:character_index + 1]
    right_part = first_string [character_index + 1:]
    new_word = left_part + right_part
    if new_word != last_word:
        print(new_word)
        last_word = new_word


