#obtains input from  user to  be  used  in a if and else statement
height= int(input("What is  your height (cm) "))

#In  this  if  and else statement we are seeing  if they are above 200cm  then they  are  tall otherwise  they are short and  if 0 and any negative interger  is inputted then  say not valid.
if height > 200:
    print("This person is very tall")

elif height <= 200 and  height > 0:
    print("This person isn't very tall")

else:
    print("Not valid")