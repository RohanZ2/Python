

def swap_remove(h_t):
    h_t_list = list(h_t)
    for i in range (len(h_t_list)-1, -1,-1):
        if h_t[i] == "H":
            try:
                if h_t_list[i+1] == "T":
                    h_t_list[i+1] = "H"
            
                else:  
                    h_t_list[i+1] == "T"
            except: IndexError
            try:
                if h_t_list[i-1] == "T":
                    h_t_list[i-1] = "H"
            
                else:
                    h_t_list[i-1] == "T"
            except: IndexError
             
            
            h_t_list.pop(i)
            break
    return ''.join(h_t_list)
            
            
            


while True:
    h_t = input("Give me H's or T's!: ")
    h_t = h_t.upper()
    
    if h_t == "H" or h_t == "T":
        print("success")
        break
    
    elif all(i in ("H," "T") for i in h_t):
        break
     
    else:
        ("try  again")


while len(h_t) >= 1:
    h_t = swap_remove(h_t)

    print(swap_remove(h_t))
    if  h_t == "H":
        print("success!")