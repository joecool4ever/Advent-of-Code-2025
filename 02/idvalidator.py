import os



# Folder where THIS script lives (01/)
script_dir = os.path.dirname(__file__)

# Parent folder (AdventOfCode/)
parent_dir = os.path.dirname(script_dir)

file_path = os.path.join(script_dir, "input.txt")

total = 0
bad_ids = []

with open(file_path, "r") as file:
    input = file.readlines()[0].split(",")
    x = 0
    for ranges in input:
        start, end = ranges.split("-")
        for i in range(int(start), int(end) + 1):
            string_i = str(i)
            digits = len(string_i)
            for j in range(digits//2, 0, -1):
                if digits % j == 0:
                    test = string_i[:j] * (digits//j)
                    if test == string_i:
                        bad_ids.append(i)
                        total += i
                        break


print("Total:", total)
print("Bad Ids:", bad_ids)