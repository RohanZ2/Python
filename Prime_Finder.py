prime_int = int(input("Give me a integer: "))


for h in range(2, prime_int + 1): #We add +1 to make sure we  are getting prime_int its  self        
    prime = True  #Assume its already  prime      
    
    for i in range(2,h):
        
        if (h % i) == 0: #Check if  its prime  or not
            prime = False     
            break
    if prime:
        print(h)