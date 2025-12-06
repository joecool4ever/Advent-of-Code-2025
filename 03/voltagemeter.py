import os

script_dir = os.path.dirname(__file__)

# Full path to input.txt in the parent folder

banks = []

for i in range(1):
    file_path = os.path.join(script_dir, "input" + str(i) +".txt")

    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            banks.append(line.strip())

    total = 0
    for bank in banks:
        digit = 0
        pointer = 0
        volt = [0] * 12

        for digit in range(12):
            # print("Digit:", digit)
            # print("Pointer is at", pointer)
            need = 12 - digit
            for j in range(pointer, len(bank) - need + 1):
                # print(j)
                if int(bank[j]) > volt[digit]:
                    volt[digit] = int(bank[j])
                    pointer = j + 1
            # print("\n")

        # print(''.join(map(str, volt)))
        total += int(''.join(map(str, volt)))
                



print("Total:", total)