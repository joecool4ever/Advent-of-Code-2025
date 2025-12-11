import os

script_dir = os.path.dirname(__file__)

# Full path to input.txt in the parent folder

inputmatrix = []
timelineMatrix = []
splits = 0

for i in range(1):
    file_path = os.path.join(script_dir, "input" + str(i) +".txt")

    inputmatrix = []
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = list(line.strip())
            inputmatrix.append(line)
            timelineMatrix.append(line)

    # start = inputmatrix[0].index('S')
    
    for i in range(1,len(inputmatrix)):
        tochange = []
        for j in range(len(inputmatrix[0])):
            if inputmatrix[i-1][j] == "|" or inputmatrix[i-1][j] == "S":
                if inputmatrix[i][j] == '.':
                    tochange.append(j)
                else:
                    splits += 1
                    if j > 0:
                        tochange.append(j - 1)
                    if j < len(inputmatrix[0]) - 1:
                        tochange.append(j + 1)

        for index in tochange:
            inputmatrix[i][index] = '|'

memo = {}

def goDownTimeline(matrix, i, j, count = 0):
    if i == len(matrix) - 1:
        return 1
    
    while matrix[i][j] != '^':
        i += 1
        if i == len(matrix) - 1:
            return 1
    if matrix[i][j] == '^':
        timelineTotal = 0
        if (i,j) in memo.keys():
            # print((i,j))
            # print("Used a memo")
            return memo[(i,j)]
        if j > 0:
            timelineTotal += goDownTimeline(matrix, i, j - 1)
        if j < len(matrix[0]) - 1:
            timelineTotal += goDownTimeline(matrix, i, j + 1)
        if (i,j) not in memo:
            memo[(i,j)] = timelineTotal
            # print(memo)
        return timelineTotal
    
def goUpTimeline(matrix, i, j):
    print(matrix[i][j], i, j)
    if matrix[i][j] == 'S':
        return 1
    if matrix[i][j] == '^':
        return 0
    if i == 0:
        return 0
    if (j < len(matrix[i]) - 1 and matrix[i][j + 1] == '^') or (j > 0 and matrix[i][j - 1] == '^'):
        timelineTotal = 0
        if j < len(matrix[i]) - 1 and matrix[i][j + 1] == '^':
            timelineTotal += goUpTimeline(matrix, i - 1, j + 1)
        if j > 0 and matrix[i][j - 1] == '^':
            timelineTotal += goUpTimeline(matrix, i - 1, j - 1)
        return timelineTotal
    else:
        return goUpTimeline(matrix, i - 1, j)


total = goDownTimeline(timelineMatrix, 0, timelineMatrix[0].index('S'))
# a
# for j in range(len(timelineMatrix[0])):
#     timelineTotal = goUpTimeline(timelineMatrix, len(timelineMatrix) - 1, j)
#     print(timelineTotal)
#     total += timelineTotal
print("Timelines:", total)
print("Splits:", splits)
