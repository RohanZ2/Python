#number_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
#for value in number_list:
#  print(value)


# The for in range statement  countsdown  from 0 to -12
for i in range(0,-12, -2):
    print(i)
# The  for in range  statement counts up from  0 to 12 with interverals of  2
for i in range(0, 12, 2):
    print(i)

for i in range(0, 100):
    if  i % 2 != 0 :
        print(i**2)
x = 0
prime = False 
#Getting  input  and  making sure they cant  enter a negative number
while x < 1:    
    pos_int = int(input("give me a positive integer: "))
    if pos_int < 0 :
        print("I SAID POSITIVE INTEGER, TRY AGAIN")
    else:
        break

if pos_int == 0 or pos_int == 1:
    print("This is not a prime number")
elif pos_int > 1:
    for i in range(2, pos_int):
        if (pos_int % i) == 0:
            prime = True
            break
    if prime:
            print(pos_int, "Is not a prime nummber")
    else:
        print(pos_int, "Is a prime number ")