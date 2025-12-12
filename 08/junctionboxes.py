import os
import math

script_dir = os.path.dirname(__file__)

# Full path to input.txt in the parent folder

boxes = []
boxesBackup = []


for i in range(1):
    file_path = os.path.join(script_dir, "input" + str(i) +".txt")

    inputmatrix = []
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            nums = line.split(",")
            nums = [int(num) for num in nums]
            boxes.append(nums)
            boxesBackup.append(nums)
    

def dist(point1, point2):
    sum = 0
    for i in range(3):
        sum += (point1[i] - point2[i])**2
    return math.sqrt(sum)

distances = {}
smallest = [0, float('inf')]
for box1 in boxes:
    for box2 in boxes:
        if box1 is not box2:
            distance = dist(box1,box2)
            distances[distance] = (box1, box2)

sortedDist = sorted(distances.keys())
xProduct = 1
circuits = []
amt_of_connects = len(sortedDist)

for i in range(amt_of_connects):
    dist = sortedDist[i]
    points = distances[dist]
    if points[0] in boxes:
        boxes.remove(points[0])
    if points[1] in boxes:
        boxes.remove(points[1])

    if circuits == []:
        circuits.append([points[0], points[1]])
    else:
        point0InCircuit = None
        point1InCircuit = None
        for circuit in circuits:
            if points[0] in circuit:
                point0InCircuit = circuit
            if points[1] in circuit:
                point1InCircuit = circuit
        if point0InCircuit and point1InCircuit:
            if point0InCircuit == point1InCircuit:
                # print("Already Accounted For")
                pass
            else:
                # print("Extending", point0InCircuit, "and", point1InCircuit)
                point0InCircuit.extend(point1InCircuit)
                circuits.remove(point1InCircuit)
        else:
            if not point0InCircuit and not point1InCircuit:
                circuits.append([points[0], points[1]])
            elif point0InCircuit and not point1InCircuit:
                point0InCircuit.append(points[1])
            elif point1InCircuit and not point0InCircuit:
                point1InCircuit.append(points[0])
    if len(circuits[0]) == len(boxesBackup):
        print(points[0], points[1])
        xProduct = points[0][0] * points[1][0]
        break


sortedCircuits = sorted(circuits, key=lambda item: len(item), reverse = True)

product = 1
# top3orLess = 3 if len(sortedCircuits) > 2 else len(sortedCircuits) - 1
# print(top3orLess)
# for i in range(3):
#     product *= len(sortedCircuits[i])
            

print("Total Circuits:", len(circuits) + len(boxes))
print("Product of Top 3:", product)
print("X Product of Last 2:", xProduct)