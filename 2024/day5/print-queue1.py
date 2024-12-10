import time
start = time.time()
total = 0
found_break = False
dependencies = {}


with open("input1.txt") as file:
    for line in file:
        if line == '\n':
            found_break = True
            continue
        if not found_break:
            numbers = line.splitlines()
            numbers = [int(number) for number in numbers[0].split('|')]
            print(numbers)
            if numbers[0] in dependencies.keys():
                dependencies[numbers[0]].append(numbers[1])
            else:
                dependencies[numbers[0]] = [numbers[1]]
        if found_break:
            line_split = [int(number) for number in line.rstrip().split(',')]
            print(line_split)
            valid = True
            # This part seems very inefficient, slower than part 2
            for index, number in enumerate(line_split):
                if number in dependencies.keys():
                    for dependency in dependencies[number]:
                        if dependency in line_split[:index]:
                            valid = False
            if valid:
                total += line_split[len(line_split)//2]


print(total)
end = time.time()
print(end - start)
