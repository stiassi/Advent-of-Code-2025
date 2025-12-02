with open("day2/ex2_input.txt") as input:
    items = input.read().strip().split(",")

invalid = 0

        
def is_repeated(value):

    item = str(value)
    digits = len(item)

    for repeat in range(2, digits+1):
        if digits % repeat != 0:
            continue

        sequence_length = digits // repeat   # length of the repeated sequence in the string
        sequence = item[:sequence_length]    # the sequence itself

        if sequence * repeat == item:  # check if repeating the sequence n times gives us the complete string again
            return True


for item in items: 

    start_str, end_str = item.split("-")
    start = int(start_str)
    end = int(end_str)

    for val in range(start, end+1):
        if item[0] == "0":  
            continue
        else:
            if is_repeated(val):
                invalid += val

print(invalid)