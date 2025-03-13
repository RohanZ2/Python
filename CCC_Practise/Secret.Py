#First two Sum
# odd = left
# even = right
# zero = same as the previous one

while True:
    #Number of instructions
    Number_of_Instructions = int(input(""))

    #has to have more than two instructions
    if Number_of_Instructions < 2:
        print("Has to have 2 or more instructions")
    else:
        break

List_Instructions = []
for _ in range(Number_of_Instructions):
    while True:
        
        Instruction = input("")
        
        if len(Instruction) < 5:
            print("has to have 5 numbers")
        else:
            break
    
    if Instruction == ("99999"):
        break
    
    List_Instructions.append(list(Instruction))
    
Previous_Direction = None

for i in  List_Instructions:
    Direction = int(i[0]) + int(i[1])
    
    if Direction == 0:
        direct = Previous_Direction
    elif Direction % 2 == 0:
        direct = "right"
    else:
        direct = "left"
        
    Previous_Direction = direct 
        
    print(direct, i[2:])