import numpy as np

total = 0
position = [0, 0]
direction = "^"
guard_map = np.empty(shape=(10, 10), dtype=str)

with open("input_small.txt") as file:
    for x, row in enumerate(file):
        stripped_row = row.rstrip()
        for y, column in enumerate(stripped_row):
            if column in {"^", ">", "v", "<"}:
                direction = column
                position = [x, y]
            guard_map[x, y] = x

# try:
#    while 1:
#        if guard_map[position[0], position[1]] != "X":
#            guard_map[position[0], position[1]] = "X"
#            total += 1
#        if direction == '^':
#            print("here")
#            if guard_map[position[0], position[1] - 1] == "#":
#                direction = '>'
#            else:
#                position[1] += 1
#        if direction == '>':
#            if guard_map[position[0] + 1, position[1]] == "#":
#                direction = 'v'
#            else:
#                position[0] += 1
#        if direction == 'v':
#            if guard_map[position[0], position[1] - 1] == "#":
#                direction = '<'
#            else:
#                position[1] -= 1
#        if direction == '<':
#            if guard_map[position[0] - 1, position[1]] == "#":
#                direction = '^'
#            else:
#                position[0] -= 1
# except:
#    print("Guard left map")

print(guard_map)
# print(position)
print(total)
