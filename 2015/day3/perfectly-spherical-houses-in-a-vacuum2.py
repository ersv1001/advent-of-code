input_file = open('input1.txt', 'r')
input = input_file.read() 
counter = 0

n1 = e1 = s1 = w1 = 0
n2 = e2 = s2 = w2 = 0

visited_locations = {'0 0': 2}

for direction in input:
    counter += 1
    if(counter % 2) == 0:
        if direction == '^':
            n2 += 1
        elif direction == '>':
            e2 += 1
        elif direction == 'v':
            s2 += 1
        elif direction == '<':  
            w2 += 1
        coordinates = str(n2-s2) + ' ' + str(e2-w2)
    else: 
        if direction == '^':
            n1 += 1
        elif direction == '>':
            e1 += 1
        elif direction == 'v':
            s1 += 1
        elif direction == '<':  
            w1 += 1
        coordinates = str(n1-s1) + ' ' + str(e1-w1)
    
    if(coordinates in visited_locations):
        visited_locations[coordinates] += 1
    else:
        visited_locations[coordinates] = 1

print(len(visited_locations))