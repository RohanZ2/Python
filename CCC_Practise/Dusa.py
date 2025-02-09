# D = Dusa starting size
starting_size = int(input("What is the starting size of the Dusa?: "))


Yobis = [] 
while True:
    Yobi = int(input("What is the size of the Yobi?: "))
    Yobis.append(Yobi)
    
    while True:
        YN = input("do you want to keep adding Yobis? (Y/N): ").strip().capitalize()
    
        
        
        if YN in ["Y","N"]:
            break
        print("try again only Y or N ")
    if YN == "N":
        break

             
for i in Yobis:
    if starting_size > i:
        starting_size += i
    if starting_size <= i:
        print(starting_size)
