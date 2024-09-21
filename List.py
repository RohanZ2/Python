#Creating  a list and variable
storage = []
i = 0

#Obtainig user input
user_list = input("What do you want to add to the list?: ")

#Putting user input in  the  list
storage += [user_list]         

#Starting  a while loop to  infitnly ask  user
while i < 6:
    
    #Infitnly ask if user if  they  want  something list until  they  n
    ask = input("do you  want to add more the the  list y|n ?: ")
    
    #If y then another  item will be added to the  list
    if  (ask == "y"):
         user_list = input("What do you want to add to the list?: ")
         storage += [user_list]         
    
    #If its n then break out of the  while loop
    elif(ask == "n"):
        break
    #If anything  else than  y  or  n  is inputted then  decline  it
    else:
        print("invalid  respone try again")
    
#Sees how  many  items are in the lsit
if (len(storage)) > 0:
    print("there is", len(storage), "items in the list")
    print("The last charchter in the string is", storage[-1])

#if theres nothing  in  the list then say  the list is empty
elif (len(storage)) <= 0:
    print("The list is  empty")