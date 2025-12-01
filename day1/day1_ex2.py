with open("day1/ex1_input.txt") as input:
    values = [line.strip() for line in input]

start = 50
counter = 0

for value in values:
    if value[0] == "L":
        for i in range(int(value[1:])):
            start = (start - 1 + 100) % 100
            if start == 0:
                counter = counter + 1
    else:
        for i in range(int(value[1:])):
            start = (start + 1) % 100
            if start == 0:
                counter = counter + 1

print(counter)