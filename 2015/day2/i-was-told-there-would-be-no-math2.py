import numpy

ribbon = 0

with open('input1.txt') as file:
    for line in file:
        dimensions = [int(x) for x in line.split('x')]
        wrap = sum(numpy.partition(dimensions, 2)[0:2])*2
        bow = numpy.prod(dimensions)
        ribbon += wrap + bow

print(ribbon)