import os
import math

script_dir = os.path.dirname(__file__)

# Full path to input.txt in the parent folder

coords = []

for i in range(2,3):
    file_path = os.path.join(script_dir, "input" + str(i) +".txt")

    inputmatrix = []
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip().split(',')
            line = [int(x) for x in line]
            coords.append(line)

largest = 0

map = [['-' for _ in range(14)] for _ in range(9)]


for coord in coords:
    i, j = coord

    map[j][i] = "X"

for row in map:
    print(row)

for i in range(len(coords)):
    for j in range(len(coords)):
        if i != j:
            coord1 = coords[i]
            coord2 = coords[j]

            print(coord1, coord2)

            inside = False
            if i < j:
                for x in range(i + 1, j):
                    print(coords[x])
                    # checkCoord = coords[x]

                    # if checkCoord[0] > coord1[0] and checkCoord[0] < coord2[0]:
                    #     if checkCoord[1] > coord1[1] and checkCoord[1] < coord2[1]:
                    #         print(checkCoord, "is inside")
                    #         inside = True
                    #         break
            elif j < i:
                for x in range(j + 1, i):
                    print(coords[x])
                    checkCoord = coords[x]

                    

                    # if checkCoord[0] > coord2[0] and checkCoord[0] < coord1[0]:
                    #     if checkCoord[1] > coord2[1] and checkCoord[1] < coord1[1]:
                    #         print(checkCoord, "is inside")
                    #         inside = True
                    #         break

            if not inside:
                print('No points between or no points inside')
                a = abs(int(coord1[0]) - int(coord2[0])) + 1
                b = abs(int(coord1[1]) - int(coord2[1])) + 1
                
                area = a * b
                if area > largest:
                    largest = area

print(largest)