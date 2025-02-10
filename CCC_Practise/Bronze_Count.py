# N = Number of participants
#Score is through 0 to 75(Included)
from collections import Counter
import heapq
participants = int(input("How many people participated?: "))

scores = []
for i in range (participants):
    while True:
        score = int(input(f"What is the score of participant {i + 1}?: "))
        if score < 0:
            print("try again, scores cannot go below 0") 
        elif score > 75:
            print("try again, scores cannot go above 75")
        else:
            break
    scores.append(score)

third = heapq.nlargest(3, scores)[-1]

repeat = scores.count(third)

print(f"{third}, {repeat}")
