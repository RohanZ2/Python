#People who have to stay together
while True:
    X = int(input(""))
    if X < 0:
        print("Try again, X must be a positive Integer!")
    else:
        break

restrict_X = []

for i in range(X):

    tog = input("")
    tog_list = tog.split()
    restrict_X.append(tog_list)

together = dict(restrict_X)
print(together)

#People who can't stay together
while True:
    Y = int(input(""))
    if Y < 0:
        print("Try again, X must be a positive Integer!")
    else:
        break

restrict_Y = []

for i in range(Y):

    tog = input("")
    canntog_list = tog.split()
    restrict_Y.append(canntog_list)

canntogether = dict(restrict_Y)
print(canntogether)


while True:
    Group = int(input(""))
    if Group < 0:
        print("Try again, X must be a positive Integer!")
    else:
        break

for l in range (Group):
    entire_group = input("")