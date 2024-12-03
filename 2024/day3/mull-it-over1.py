import re
mul_list = []
total = 0

with open("input1.txt") as file:
    for line in file:
        mul_list.append(re.findall("(mul\([0-9]+,[0-9]+\))", line))
    flat_mul_list = [
        x
        for xs in mul_list
        for x in xs
    ]
    print(flat_mul_list)
    for mul in flat_mul_list:
        numbers = re.sub('[^0-9,]', '', mul)
        split_mul = mul.split(',')
        total = int(split_mul[0]) * int(split_mul[1])

print("total = ", total)
