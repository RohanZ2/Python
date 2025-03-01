# Gets a non negative integer
while True:
    N = int(input())
    if N < 0:
        print("Try Again")
    else:
        break

#New list
New_codes = []
for i in range(N):
    #orginal input of user
    Orignal = input()
    
    for i in Orignal:
        New_codes.append(i)

digits = []
#new string to collect numbers
num = ""
#Collects both the length and charchters of the barcode
for d, char in enumerate(New_codes):
    
    #Checks if its a digit, or a negative
    if char.isdigit() or (char  == "-" and d < len(New_codes) - 1 and New_codes[d + 1].isdigit()):
        num += char

    else:
        if num:
            digits.append(num)
            num = ""
if num:
    digits.append(num)
        
Sorted_codes = []
for l in New_codes:
    digit  = l.isdigit()
    if digit:
        New_codes.remove(l)
    
    if not l.isdigit():
        Sorted_codes.append(ord(l))

        for h in Sorted_codes:
            if h == 45:
               Sorted_codes.remove(45)
            for k in range(97, 123):
                
                if h == k:
                    Sorted_codes.remove(k) 

sum_of_digits = sum(map(int, digits))

normal_code = []

for i in Sorted_codes:
    normal_code.append(chr(i))

final = "".join(normal_code) + str(sum_of_digits)

print(final)