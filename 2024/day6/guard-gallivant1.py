import numpy as np

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
            guard_map[x, y] = column


print(guard_map)
print(position)
