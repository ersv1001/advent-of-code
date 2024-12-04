import re
import numpy as np

input = []
total_words = 0

with open("input1.txt") as file:
    for line in file:
        temp_list = []
        for letter in line:
            if letter != "\n":
                temp_list.append(letter)
        input.append(temp_list)

print(input)
np_input = np.array(input)

with open("input1.txt") as file:
    for line in file:
        total_words += len(re.findall("XMAS", line))

print(total_words)
