import os

script_dir = os.path.dirname(__file__)

# Full path to input.txt in the parent folder



for i in range(1):
    file_path = os.path.join(script_dir, "input" + str(i) +".txt")

    ranges = []
    ids = []

    with open(file_path, "r") as file:
        lines = file.readlines()
        splitter = lines.index('\n')
        ranges = lines[:splitter]
        ids = lines[splitter + 1:]
        ranges = [[int(ranges[x].strip().split("-")[0]), int(ranges[x].strip().split("-")[1])] for x in range(len(ranges))]
        ids = [int(ids[x].strip()) for x in range(len(ids))]

    validIds = 0
    freshIds = 0
    for id in ids:
        valid = False
        for range_ in ranges:
            valid = id >= range_[0] and id <= range_[1]
            if valid:
                validIds += 1
                break
    
    changes = 1
    ignore = [0,-1]
    while changes:
        changes = 0
        for i in range(len(ranges)):
            if ranges[i] != [0,-1]:
                for j in range(i + 1, len(ranges)):
                    if ranges[i] != [0,-1]:
                        range1 = ranges[i]
                        range2 = ranges[j]
                        if range1[0] <= range2[0]:
                            # Already accounted for
                            if range1[1] >= range2[1]:
                                ranges[j] = [0,-1]
                                changes += 1
                            # right extension
                            elif range1[1] >= range2[0] and range1[1] <= range2[1]:
                                ranges[i][1] = range2[1]
                                ranges[j] = [0,-1]
                                changes += 1
                        elif range1[0] > range2[0]:
                            if range1[0] <= range2[1]:
                                if range1[1] <= range2[1]:
                                    ranges[i] = ranges[j]
                                    ranges[j] = [0,-1]
                                    changes += 1
                                elif range1[1] >= range2[1]:
                                    ranges[i][0] = ranges[j][0]
                                    ranges[j] = [0,-1]
                                    changes += 1
                            
    total = 0
    for range_ in ranges:
        total += len(range(range_[0], range_[1] + 1))
    print("Total:", total)
