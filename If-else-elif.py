#get a mark from the user

mark = int(input("Enter a mark:"))   



# determine the letter grade

if mark <= 100 and mark >= 80:
    print("A mark of", mark, "is an A.")

elif mark < 80 and mark >= 70:
    print("A mark of", mark, "is a B.")

elif mark < 70 and mark >= 60:
    print("A mark of", mark, "is a C")
    
elif mark < 60 and mark >= 50:
    print("A mark of ", mark, "is a  D")

elif mark < 50 and mark >= 0:
    print("FAIL")

else:

 print("This is not a valid mark.")