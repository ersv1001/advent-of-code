input_file = open('input1.txt', 'r')
input = input_file.read() 

n = e = s = w = 0
visited_locations = {'0 0': 1}

for direction in input:
    if direction == '^':
        n += 1
    elif direction == '>':
        e += 1
    elif direction == 'v':
        s += 1
    elif direction == '<':  
        w += 1
    coordinates = str(n-s) + ' ' + str(e-w)
    
    if(coordinates in visited_locations):
        visited_locations[coordinates] += 1
    else:
        visited_locations[coordinates] = 1

print(len(visited_locations))