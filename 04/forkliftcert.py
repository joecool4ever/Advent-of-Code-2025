import os

script_dir = os.path.dirname(__file__)

# Full path to input.txt in the parent folder

matrix = []

for i in range(1,2):
    file_path = os.path.join(script_dir, "input" + str(i) +".txt")

    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            matrix.append(list(line.strip()))

answer = 0

changeMatrix = [row[:] for row in matrix]
changeInRolls = 1
runs = 0
while changeInRolls !=0:
    runs += 1
    changeInRolls = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            rolls = 0
            if matrix[i][j] == '@':
                if j != 0:
                    if i != 0:
                        rolls += (matrix[i - 1][j - 1] == '@')
                    rolls += (matrix[i][j - 1] == '@')
                    if i != len(matrix[i]) - 1:
                        rolls += (matrix[i + 1][j - 1] == '@')
                if i != 0 :
                    rolls += (matrix[i - 1][j] == '@')
                if i != len(matrix[i]) - 1:
                    rolls += (matrix[i + 1][j] == '@')
                if j != len(matrix) - 1:
                    if i != 0:
                        rolls += (matrix[i - 1][j + 1] == '@')
                    rolls += (matrix[i][j + 1] == '@')
                    if i != len(matrix[i]) - 1:
                        rolls += (matrix[i + 1][j + 1] == '@')
                
                if rolls < 4:
                    changeInRolls += 1
                    answer += 1
                    changeMatrix[i][j] = "X"
    # print('\n')
    # print("Run:", runs, "Removed", changeInRolls, "rolls of paper")
    matrix = [row[:] for row in changeMatrix]
    # for row in changeMatrix:
    #     print(row)

print("Answer:", answer)