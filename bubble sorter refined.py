from graphics import *
from random import randint
import time

#initialise


print("give amount of data")
length = int(input())
win = GraphWin("data", length + 100, 500)
lines = [None] * length
height = [None] * length
place = [None] * length
done = False


def swapLines(line1, line2):
    #remove lines
    lines[line1].undraw()
    lines[line2].undraw()
    #swap heights but keep x values same
    lines[line1] = Line(Point(place[line1], 500), Point(place[line1], 500-height[line2]))
    lines[line2] = Line(Point(place[line2], 500), Point(place[line2], 500-height[line1]))
    #changing heights in height list
    ph1 = height[line1]
    ph2 = height[line2]
    height[line1] = ph2
    height[line2] = ph1
    #redraw lines
    lines[line1].draw(win)
    lines[line2].draw(win)



#create the data
for i in range(length):
    height[i] = randint(1,500)
    place[i] = i+50
    lines[i] = Line(Point(place[i], 500), Point(place[i], 500-height[i]))
    lines[i].draw(win)
    lines[i].setOutline("red")
    lines[i].setOutline("black")


print("Enter in anything to start sorting")
dummyvariable = input()

while done == False:
    couldBeDone = True
    for i in range(length-1):
        #lines[i].setOutline("red")
        if height[i] > height[i+1]:
            #j = i+1
            swapLines(i, i+1)
            couldBeDone = False
        #lines[i].setOutline("black")
    if couldBeDone == True:
        done = True

#now it is done
print("sorted")
for i in range(length-1):
    if height[i] <= height[i+1]:
        lines[i].setOutline("green")
    else:
        print("sike nope not sorted")
        lines[i].setOutline("red")

print("Enter in anything to close")
dummyvariable = input()