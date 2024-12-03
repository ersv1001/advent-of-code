import re
total = 0

with open("input1.txt") as file:
    data = file.read().replace('\n', '')

    subbed_line = re.sub("(don't\(\).*?((do\(\))+|$))", '', data)
    mul_list = re.findall("(mul\([0-9]+,[0-9]+\))", subbed_line)

    for mul in mul_list:
        numbers = re.sub('[^0-9,]', '', mul)
        split_mul = numbers.split(',')
        total += int(split_mul[0]) * int(split_mul[1])

print("total = ", total)
