b = 0
col = int(input("how many coloums do you need: "))
row = int(input("How many rows do you need: ")) 
arr = [[0] * col for _ in range(row)]

for i in range(row):
    for j in range(col):
        arr[i][j] = int(input(f"Enter a number for position ({i+1}, {j+1}): "))

for  row  in  arr:
    print(row)