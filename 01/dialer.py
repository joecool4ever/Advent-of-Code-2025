import os



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
                
                if dir == "L":
                    if x == 0:
                        x = 100
                    if amt >= x:
                        # print("password increasing by", 1 * amt % 100 + (amt // 100))
                        if amt % 100 != 0:
                            password += 1
                        password += amt // 100
                    # print("Subtracting", amt % 100, "from", x)
                    x = x - (amt % 100)
                    if x < 0:
                        x = 100 + x
                    
                if dir == "R":
                    if amt >= 100 - x:
                        # print("password increasing by", 1 + ((amt - (100 - x))//100))
                        if (amt - (100 - x)) % 100 != 0:
                            password += 1
                        password += ((amt - (100 - x))//100)

                    x = x + (amt % 100)
                    # print("Adding", amt % 100, "to", x)
                    x = x % 100
                # print(x)
                

    print(str(i) + ". Password =", password)
