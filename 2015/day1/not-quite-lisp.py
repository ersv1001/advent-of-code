input_file = open('input1.txt', 'r')
input = input_file.read() 
count = 0
position = 0
positionFound = False

for bracket in input:
    position += 1
    if bracket == '(':
        count += 1
    if bracket == ')':
        count -= 1
        if not positionFound and count < 0:
            print('Basement found at:', position)
            positionFound = True

print('Final floor:', count)