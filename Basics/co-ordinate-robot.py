#https://www.mathplayground.com/SaveTheZogs/index.html
# Open this link only in Edge browser( Google Chrome might not support)
#Use Euclidean Distance Formula to find distance between 2 points

import math
pos = [0,0]
while True:
    s = input(' Enter in the form of Direction and steps')
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass

print (math.sqrt(pos[1]**2+pos[0]**2))
