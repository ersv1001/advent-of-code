total_value = 0

with open('input1.txt') as file:
    for line in file:
        dimensions = [int(x) for x in line.split('x')]
        values = [dimensions[0]*dimensions[1], dimensions[1]*dimensions[2], dimensions[2]*dimensions[0]]
        total_value += 2*(sum(values)) + min(values)

print(total_value)