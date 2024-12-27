import  math

def distance (ax,ay,bx,by):
    #calculaing t
    return math.sqrt((bx-ax)**2+(by-ay)**2)

def area(ax, ay, bx, by, cx, cy):
    #calculating the area for any triangle with geometry 
    return abs((1 / 2) * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by)))

def calc ():
    #calculating the area for distance 
    distance1 = distance(ax, ay, bx, by)
    distance2 = distance(ax, ay, cx, cy)
    distance3 = distance(bx, by, cx, cy)

    #Calculating the total area and then calculating the area for the triangle. a1, a2, and a3 are to calculate the point with the triangle points to see if all the areas those make, make up a triangle
    a = area(ax, ay, bx, by, cx, cy)
    a1 = area(px, py, ax, ay,bx, by)
    a2 = area(px,py,bx,by,cx,cy)
    a3 = area(px,py,ax,ay,cx,cy)
    
    return distance1, distance2, distance3, a, a1, a2, a3



#Getting user input for the points.
ax = int(input("Please enter a positive input for point ax: "))
ay = int(input("Please enter a positive input for point ay: "))
bx = int(input("Please enter a positive input for point bx: "))
by = int(input("Please enter a positive input for point by: "))
cx = int(input("Please enter a positive input for point cx: "))
cy = int(input("Please enter a positive input for point cy: "))
px = int(input("Please enter a positive input for test  point X: "))
py = int(input("Please enter a positive input for test point Y: "))

#calling the function to get the varibales
distance1, distance2, distance3, a, a1, a2, a3 = calc()


#checking if the point lies in the triangle
if a1 + a2 + a3 == a:
    print("The point lies in the triangle.")
else:
    print("The point does not lie in the triangle.")