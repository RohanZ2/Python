# find the maximum element in a list 

numbers = []
# this is the same as 
# num = int(input("Enter a number:"))
# numbers.append(num)

numbers.append(int(input("Enter a number:")))
numbers.append(int(input("Enter a second number:")))
numbers.append(int(input("Enter a third number:")))
numbers.append(int(input("Enter a fourth number:")))

# print the list in order and also in reverse order
print(numbers)
numbers.reverse()
print(numbers)

maxNum = numbers[0]
if numbers[0] >= numbers[1] and numbers[0] >= numbers[2] and numbers[0] >= numbers[3]:
  maxNum = numbers[0]
  
if numbers[1] >= numbers[2] and numbers[1] >= numbers[3] and  numbers [1] >= numbers[0]:
  maxNum = numbers[1]
  
if numbers[2] >= numbers[3] and numbers[2] >= numbers[1] and  numbers[2] >= numbers[0]:
    maxNum = numbers[2]

if numbers[3] >= numbers[2] and numbers[3] >= numbers[1]and numbers[3] >= numbers[0]:
    maxNum = numbers[3]

print("The maximum element of", numbers, "is",maxNum)