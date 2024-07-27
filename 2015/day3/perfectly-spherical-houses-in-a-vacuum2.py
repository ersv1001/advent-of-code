input_file = open("input1.txt", "r")
input = input_file.read()
visited_locations = {}


def move(coordinates, direction):
    if direction == "^":
        coordinates[1] += 1
    elif direction == ">":
        coordinates[0] += 1
    elif direction == "v":
        coordinates[1] -= 1
    elif direction == "<":
        coordinates[0] -= 1
    print(coordinates)
    if (coordinates[0], coordinates[1]) not in visited_locations:
        visited_locations[coordinates[0], coordinates[1]] = 1


turn_counter = 0
coordinates1 = [0, 0]
coordinates2 = [0, 0]


for direction in input:
    turn_counter += 1
    if (turn_counter % 2) == 0:
        move(coordinates2, direction)
    else:
        move(coordinates1, direction)


print(len(visited_locations))
