# get input from the user 

while True:
    letter = input("Enter a letter:")

    if letter.isalpha() == False or len(letter) > 1:
        print("Please enter a single letter.")

    else:
        letter = letter.upper()
        break
#Ord(Letter) - Whats happening  is im getting the ACSII value of the letter, e.g A is 65.
#the reason for - is so that i  can get the numbers  of  rows and coloums i need
numRows = ord(letter) - ord("A") + 1

for row in range(numRows):

    for col in range(numRows -  row):
        print(chr(ord("A")+ col), end="")
    print()