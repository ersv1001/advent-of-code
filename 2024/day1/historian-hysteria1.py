list1 = []
list2 = []

with open("input1.txt") as file:
    for line in file:
        locations = line.split("   ")
        list1.append(int(locations[0]))
        list2.append(int(locations[1]))

list1.sort()
list2.sort()
distance = 0

for index, _ in enumerate(list1):
    distance += abs(list1[index] - list2[index])

print(distance)
