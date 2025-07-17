# Advent of Code 2023 - Day 1 Solution

# initializing the result variable and a list with all digits spelled out
final_result = 0

# very ugly if-branching to find spelt out digits
def is_spelled_out(check_string, mode):
    if mode == 'left' and check_string[0] in ['o', 't', 'f', 's', 'e', 'n']:
        if check_string.startswith('one'):
            return '1'
        elif check_string.startswith('two'):
            return '2'
        elif check_string.startswith('three'):
            return '3'
        elif check_string.startswith('four'):
            return '4'
        elif check_string.startswith('five'):
            return '5'
        elif check_string.startswith('six'):
            return '6'
        elif check_string.startswith('seven'):
            return '7'
        elif check_string.startswith('eight'):
            return '8'
        elif check_string.startswith('nine'):
            return '9'
        else:
            return None
    elif mode == 'right' and check_string[-1] in ['e', 'o', 'r', 'x', 'n', 't']:
        if check_string.endswith('one'):
            return '1'
        elif check_string.endswith('two'):
            return '2'
        elif check_string.endswith('three'):
            return '3'
        elif check_string.endswith('four'):
            return '4'
        elif check_string.endswith('five'):
            return '5'
        elif check_string.endswith('six'):
            return '6'
        elif check_string.endswith('seven'):
            return '7'
        elif check_string.endswith('eight'):
            return '8'
        elif check_string.endswith('nine'):
            return '9'
        else:
            return None
    else:
        return None

# iterate through line from the left side until numeric char is found
def get_first_digit(input_line):
    line_len = len(input_line)
    iteration = 0
    while line_len != iteration:
        if input_line[0].isdigit():
            return input_line[0]
        else:
            check_spelled_out = is_spelled_out(input_line, 'left')
            if check_spelled_out:
                return check_spelled_out
            input_line = input_line[1:]
            iteration += 1
    return None

# iterate through the line from the right until numeric char is found
def get_last_digit(input_line):
    line_len = len(input_line)
    iteration = 0
    while line_len != iteration:
        if input_line[-1].isdigit():
            return input_line[-1]
        else:
            check_spelled_out = is_spelled_out(input_line, 'right')
            if check_spelled_out:
                return check_spelled_out
            input_line = input_line[:-1]
            iteration += 1
    return None


with open ("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        number = get_first_digit(line)
        number = number + get_last_digit(line)
        # convert number string to integer to allow for proper calculation
        number = int(number)
        final_result = final_result + number
    print(f"The final result is: {final_result}")



