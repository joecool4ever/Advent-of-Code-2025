import os

script_dir = os.path.dirname(__file__)

# Full path to input.txt in the parent folder

for i in range(6):
    x = 50
    password = 0
    file_path = os.path.join(script_dir, "input" + str(i) +".txt")
    print(x)

    with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                move = line.strip()
                dir = move[0]
                amt = int(move[1:])
                rem = amt % 100
                password += amt // 100
                
                if dir == "L":
                    if x == 0:
                        x = 100
                    x = x - rem
                    if x <= 0:
                        password += 1
                        x = 100 + x
                    
                if dir == "R":
                    if x == 100:
                        x = 0

                    x = x + rem
                    if x >= 100:
                        password += 1
                        x = x % 100

                # if x == 0:
                #     password += 1
                

    print(str(i) + ". Password =", password)
