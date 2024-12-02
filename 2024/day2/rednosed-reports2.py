count = 0


def check_report(report):
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
        return True


with open("input1.txt") as file:
    for line in file:
        report_strings = line.split()
        report = [int(num) for num in report_strings]
        print(report)
        if check_report(report):
            count += 1
        else:
            for index, number in enumerate(report):
                rep = report.copy()
                print(index)
                del rep[index]
                if check_report(rep):
                    count += 1
                    break


print(count)
