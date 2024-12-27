num = 0
while True:
    value = input("Enter an integer:")

    if value.isdigit() == False:
        print(value, "has non-numeric input")
	
    elif int(value) <= 0:
        print(value, "needs to be positive")
    else:
        num = int(value)
        break

if num == 1:
    print(1)

elif num == 2:
    print(1)
    print(1)


prev = 1
prevPrev = 1
current = prevPrev
for term in range( 1, num+1):
    print(current)
    prev, prevPrev = prevPrev, current
    current = prev + prevPrev # 1 + 1 = 2