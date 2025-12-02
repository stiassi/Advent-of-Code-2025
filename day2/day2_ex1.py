with open("day2/ex2_input.txt") as input:
    items = input.read().strip().split(",")

invalid = 0

def is_double(value):
    item = str(value)
    if len(item) % 2 != 0:
        return False
    else:
        half = len(item) // 2 
        compare = item[:half] == item[half:]
        return compare


for item in items: 

    start_str, end_str = item.split("-")
    start = int(start_str)
    end = int(end_str)

    for val in range(start, end+1):
        if item[0] == "0":  
            continue
        else:
            if is_double(val):
                invalid += val
    

print(invalid)