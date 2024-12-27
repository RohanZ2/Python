sentence = input("Write down a sentence!: ")
sentence = sentence.lower()
sentence = sentence.replace(" ", "")

letters = []
dupes = []

for i in sentence:
    if i not in letters:
        letters.append(i)
        count  = sentence.count(i)
        dupes.append((i, count))
        
        

for char, count  in dupes:
    print("The character", char,"occurred", count, "time(s)")