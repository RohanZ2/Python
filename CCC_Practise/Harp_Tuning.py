# A - T
# + -
# Positive Integer

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]

first = input("What is the tuning Instrutions?: ")
list_first = list(first)

f = [t.replace("+", " tighten ").replace("-", " loosen ") for t in list_first]

output_list = []
for char in f:
    output_list.append(char)
    if char.isnumeric():
        output_list.append("\n")

output = "".join(output_list)

print(output) 
    

        
    




        


