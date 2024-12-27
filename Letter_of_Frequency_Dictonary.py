user_input = input("Write down a sentence: ")
user_input = user_input.upper()
user_input = user_input.replace(" ", "")


letter_count = {}

for letter in user_input:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1
        
        
for letter, count in letter_count.items():
        print(f"{letter} appears {count} times(s).")