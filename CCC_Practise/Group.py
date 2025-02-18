while True:
    X = int(input(""))
    if X < 0:
        print("Try again, X must be a positive Integer!")
    else:
        break

together = {}
restrict = []

for i in range(X):

    tog = input("")
    tog_list = tog.split()
    restrict.append(tog_list)

d = dict(restrict)
print(d)
