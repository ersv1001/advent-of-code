import re

grid = [[0 for x in range(1000)] for x in range(1000)]


def handle_switch(x, y, instruction):
    if instruction == "on":
        grid[x][y] = 1
    if instruction == "off":
        grid[x][y] = 0
    if instruction == "toggle":
        if grid[x][y] == 0:
            grid[x][y] = 1
        else:
            grid[x][y] = 0


with open("input1.txt") as file:
    for line in file:
        instruction = "toggle"
        if "on" in line:
            instruction = "on"
        elif "off" in line:
            instruction = "off"
        print(line)
        line = re.sub("[a-zA-Z]|(?<![0-9])\s", "", line)
        line = re.sub("\s", ",", line)
        numbers = line.split(",")
        print(numbers)
        x1 = int(numbers[0])
        y1 = int(numbers[1])
        x2 = int(numbers[2])
        y2 = int(numbers[3])

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                handle_switch(x, y, instruction)

sum = 0
for x in range(1000):
    for y in range(1000):
        if grid[x][y]:
            sum = sum + 1
print(sum)
