list1 = []
list2 = []

with open("input1.txt") as file:
    for line in file:
        locations = line.split("   ")
        list1.append(int(locations[0]))
        list2.append(int(locations[1]))

similarity_score = 0

for id1 in list1:
    for id2 in list2:
        if id1 == id2:
            similarity_score += id1


print(similarity_score)
