from functools import cmp_to_key
import time
start = time.time()
total = 0
found_break = False
dependencies = {}


def compare(x, y):
    if x in dependencies.keys():
        if y in dependencies[x]:
            return - 1
    if y in dependencies.keys():
        if x in dependencies[y]:
            return 1
    else:
        return 0


with open("input1.txt") as file:
    for line in file:
        if line == '\n':
            found_break = True
            continue
        if not found_break:
            numbers = line.splitlines()
            numbers = [int(number) for number in numbers[0].split('|')]
            if numbers[0] in dependencies.keys():
                dependencies[numbers[0]].append(numbers[1])
            else:
                dependencies[numbers[0]] = [numbers[1]]
        if found_break:
            line_split = [int(number) for number in line.rstrip().split(',')]
            sorted_line_split = sorted(line_split, key=cmp_to_key(compare))
            if line_split != sorted_line_split:
                print(sorted_line_split)
                total += sorted_line_split[len(sorted_line_split)//2]

print(total)
end = time.time()
print(end - start)
