import os

script_dir = os.path.dirname(__file__)

# Full path to input.txt in the parent folder

for i in range(1):
    file_path = os.path.join(script_dir, "input" + str(i) +".txt")

    inputmatrix = []
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            # line = line.strip()
            line = [x for x in line if x != "\n"]
            inputmatrix.append(line)

    # for row in inputmatrix:
    #     print(row)
    bank = []
    total = 0
    evalcolumnTotal = 1
    for j in range(len(inputmatrix[0])-1, -1, -1):
        num = ""
        for i in range(len(inputmatrix)):
            # print("row:", i, "col:", j)
            if i < len(inputmatrix) - 1:
                # print("adding", inputmatrix[i][j])
                num += inputmatrix[i][j]
            elif num.strip() == '':
                break
            else:
                if inputmatrix[i][j] == ' ':
                    bank.append(num)
                else:
                    bank.append(num)
                    # print(bank)
                    if inputmatrix[i][j] == '+':
                        evalcolumnTotal -= 1
                    for num in bank:
                        # print(int(num))
                        if inputmatrix[i][j] == '+':
                            evalcolumnTotal += int(num)
                        elif inputmatrix[i][j] == '*':
                            evalcolumnTotal *= int(num)
                    # print("evalcolumnTotal=", evalcolumnTotal)
                    total += evalcolumnTotal

                    bank = []
                    evalcolumnTotal = 1
                    
            
    # for j in range(len(inputmatrix[i])):
    #     eval = inputmatrix[len(inputmatrix) - 1][j]
    #     # print(eval)
    #     if eval == "*":
    #         result = 1
    #     else:
    #         result = 0
    #     for i in range(len(inputmatrix) - 1):
    #         if eval == "*":
    #             result *= int(inputmatrix[i][j])
    #         elif eval == "+":
    #             result += int(inputmatrix[i][j])    
    #     total += result

    print("Total:", total)
            

