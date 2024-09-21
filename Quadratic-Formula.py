a = int(input("what is  your first number: "))
b = int(input("what is  your second number: "))
c = int(input("what is  your third number: "))

print("the  equation is  Ax ** 2 + Bx + C = 0")

discriminant  = b**2 - 4*a*c

if discriminant > 0:
    x1 = (-b + (discriminant)**0.5)  / (2*a)
    x2 = (-b - (discriminant)**0.5) / (2*a)
    print("The roots are real: x1 =",x1, "x2 =", x2 )
    
elif discriminant == 0:
    x1 = -b/(2*a)
else:
    real_part = -b / (2*a)
    imaginary_part = (abs(discriminant)**0.5) / (2*a)
    print("The roots are complex: x1 = ", real_part + imaginary_part,"i", "x2 =", real_part - imaginary_part,"i")