def split_sort(nums):
    if len(nums) > 1: # if  there is  something in the list then  continue
        mid = len(nums) // 2 #find  the middle point of the list
        
        right_half = nums[mid:]  #right  side of the list(Including the mid point)
        left_half = nums[:mid] #left side of the list(not including  mid point)
        
        split_sort(left_half) #split even  further(recursion) to get 1 number
        split_sort(right_half) #Splits even further(recursion) to  get 1 number
        
        i = 0
        j = 0
        k = 0
        
        while i < len(left_half) and j < len(right_half):
            """
            A while loop that sorts out the  indiduals numbers and puts 
            them in  order while joining them  together
            """

            if left_half[i] > right_half[j]:
                    nums[k] = left_half[i]
                    i += 1


            else:
                nums[k] = right_half[j]
                j+= 1
            k += 1
                
        while i < len(left_half):
            nums[k] = left_half[i]  
            i += 1
            k += 1


        while j < len(right_half):
            nums[k] = right_half[j]
            j += 1
            k += 1




nums = []
while True:
    num = int(input("What numbers do you want to sort? if you want to break enter 0: "))
    nums.append(num)
    if num == 0:
        break
split_sort(nums)

print("Sorted array", nums)