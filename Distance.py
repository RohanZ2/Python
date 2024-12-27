import datetime
import math

def distance (a1, b1, a2, b2):
    """
    Formula  for  finding the  distance between two
    points
    """
    
    return math.sqrt((a2-a1) ** 2 + (b2-b1)) ** 2

longitude1 = float(input("what is the longitude of the current place your are in: "))
latitude1 = float(input("what is the laitude of the current place your are in:" ))
longitude2 = float(input("what is the longitude of the place your are going to be in: "))
latitude2 = float(input("what is the laitude of the place your are going to be in: "))

while True:
    current = input("What is the date currently? (YYYY-MM-DD): ")
    event = input("What day is the event happening?: (YYYY-MM-DD): ")
    
    try: # Making  sure that the input is in  the correct format, (YYYY-MM-DD)
        current_date = datetime.datetime.strptime(current, "%Y-%m-%d")
        event_date = datetime.datetime.strptime(event, "%Y-%m-%d")
        break
    
    except ValueError:
        print("Invalid format. please enter it like this: YYYY-MM-DD.")

days_until_event = (event_date - current_date).days

dist = distance(latitude1, longitude1, latitude2, longitude2)

print(f"The distance to the event location is: {dist:.2f}")
print(f"The number of days until the event is: {days_until_event}")