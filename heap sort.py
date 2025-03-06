from graphics import *
from random import randint
import time
import math
from math import floor

created = False
wait = "idk"
#initialise
print("give amount of data")
while created == False:
    try:
        length = int(input())
        if length > 0:
            created = True
        else:
            print("please enter a natural number")
    except:
        print("please enter a natural number")
print("do you want it to pause or not")
while wait == "idk":
    m = input()
    if m == "yes":
        wait = True
    elif m == "no":
        wait = False
    else:
        print("Please enter in yes or no no caps")
win = GraphWin("data", length+100, 500)



lines = [None] * length
height = [None] * length
#height = [324, 456, 474, 429, 215, 65, 262, 428, 227]
place = [None] * length
done = False
lowest = 0
sortedLength = 0
shrink = 1.3

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

time.sleep(2)

gap = floor(length/shrink)

def findChild(linePlace,number):
    actualPlace = linePlace + 1
    binaryTreePlace = math.log(actualPlace,2)
    pBranch = floor(binaryTreePlace)
    pLeaf = actualPlace - 2**pBranch
    cBranch = pBranch + 1
    cLeaf = pLeaf * 2
    if number == 1:
        return 2**cBranch + cLeaf - 1
    else:
        return 2**cBranch + cLeaf


def compareWithChildren(linePlace,limit):
    actualPlace = linePlace + 1
    binaryTreePlace = math.log(actualPlace,2)
    pBranch = floor(binaryTreePlace)
    pLeaf = actualPlace - 2**pBranch
    cBranch = pBranch + 1
    cLeaf = pLeaf * 2

    c1 = 2**cBranch + cLeaf -1
    c2 = c1 + 1
    if c1 < limit:
        if height[c1] > height[linePlace]:
            if c2 < limit:
                if height[c1] > height[c2]:
                    return "child1"
                else:
                    return "child2"
            else:
                return "child1"
        elif c2 < limit:
            if height[c2] > height[linePlace]:
                return "child2"
            else:
                return "parent"
        else:
            return "parent"
    else:
        return "parent"


    
""""""
#heap sort
#heapify

lastLeaf = 2**floor(math.log(length,2))-1

for i in range(lastLeaf):
    sectionDone = False
    currentCheck = lastLeaf - i-1
    while sectionDone == False:
        greatest = compareWithChildren(currentCheck,length)
        if greatest == "parent":
            sectionDone = True
        elif greatest == "child1":
            tempCheck = currentCheck
            currentCheck = findChild(currentCheck,1)
            swapLines(tempCheck, findChild(tempCheck,1))
        elif greatest == "child2":
            tempCheck = currentCheck
            currentCheck = findChild(currentCheck,2)
            swapLines(tempCheck, findChild(tempCheck,2))

if wait == True:
    time.sleep(2)
    
# now actually sort pls
for i in range(length-1):
    swapLines(0,length-(i+1))
    sectionDone = False
    currentCheck = 0
    while sectionDone == False:
        greatest = compareWithChildren(currentCheck,length-i-1)
        if greatest == "parent":
            sectionDone = True
        elif greatest == "child1":
            tempCheck = currentCheck
            currentCheck = findChild(currentCheck,1)
            swapLines(tempCheck, currentCheck)
        elif greatest == "child2":
            tempCheck = currentCheck
            currentCheck = findChild(currentCheck,2)
            swapLines(tempCheck, currentCheck)
"""

#selection
for i in range(length):
    lowest = 0
    lines[lowest].setOutline("red")
    lines[length-1-i].setOutline("red")
    for j in range(length-i):
        if height[j] < height[lowest]:
            lines[lowest].setOutline("black")
            lowest = j
            lines[lowest].setOutline("red")
    if height[lowest] != height[length-1-i]:
        swapLines(lowest,length-i-1)
    lines[lowest].setOutline("black")
    lines[length-1-i].setOutline("black")
"""


#now it is done
print("sorted")
for i in range(length-1):
    if height[i] <= height[i+1]:
        lines[i].setOutline("green")
        lines[i+1].setOutline("green")
    else:
        print("sike nope not sorted")
        lines[i].setOutline("red")

"""
for i in range(length):
    lines[i].undraw()
"""
