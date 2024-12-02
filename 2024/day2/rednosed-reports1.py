count = 0

with open("input1.txt") as file:
    for line in file:
        report_strings = line.split()
        report = [int(num) for num in report_strings]
        print(report)
        increasing = True
        decreasing = True
        adjacent_ok = True
        for index, number in enumerate(report):
            if index == 0:
                continue
            prev = report[index-1]
            if number >= prev:
                decreasing = False
            if number <= prev:
                increasing = False
            if abs(number - prev) > 3:
                adjacent_ok = False
        if (increasing or decreasing) and adjacent_ok:
            count += 1

print(count)
