import re

file_input = input("Enter file name:")
fh = open(file_input)
Num = []

for line in fh:
    line = line .rstrip()
    x = re.findall("([0-9]+)", line)

    if len(x) < 1: continue

    for i in range(len(x)):
        numbers = float(x[i])
        y = Num.append(numbers)

print(sum(Num))