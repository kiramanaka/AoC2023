# Advent of Code 2023 - Day 3 Solution

# import deque to allow for faster left pops in lists
from collections import deque
from operator import mul

# initialize final result
final_result = 0


def find_serial_numbers(buffer):
    number_sum = 0
    # skip the first execution to have visibility over two lines
    if not buffer[1]:
        return None
    else:
        index = 0
        for char in buffer[1]:
            detection = {
                'top_left': False,
                'top': False,
                'top_right': False,
                'left': False,
                'right': False,
                'bottom_left': False,
                'bottom': False,
                'bottom_right': False,
            }
            # skip detection if the current char is a number or a dot
            if char == '.' or char.isdecimal():
                index += 1
                continue
            # if the current char is a star, run detection
            elif char == '*':
                if buffer[0]:
                    if buffer[0][index - 1].isdigit():
                        detection['top_left'] = True
                    if buffer[0][index].isdigit():
                        detection['top'] = True
                    if buffer[0][index + 1].isdigit():
                        detection['top_right'] = True
                if buffer[1][index - 1].isdigit():
                    detection['left'] = True
                if buffer[1][index + 1].isdigit():
                    detection['right'] = True
                if buffer[1]:
                    if buffer[2][index - 1].isdigit():
                        detection['bottom_left'] = True
                    if buffer[2][index].isdigit():
                        detection['bottom'] = True
                    if buffer[2][index + 1].isdigit():
                        detection['bottom_right'] = True
                # if serials were detected, pass on to parser
                if any(detection.values()):
                    numbers = parse_detection(buffer, detection, index)
                    number_sum += numbers
                index += 1
            else:
                index += 1
                continue

        return number_sum

# read the surrounding numbers and multiply them if EXACTLY 2 numbers were found
def parse_detection(buffer, detection, index):
    serials = []
    # read the top row for detections
    if detection['top_left'] or detection['top'] or detection['top_right']:
        if detection['top'] and detection['top_left'] and detection['top_right']:
            serials.append(int(buffer[0][index - 1:index + 2].strip('.')))
        elif not detection['top']:
            if detection['top_left']:
                serials.append(int(buffer[0][index - 3:index].strip('.')))
            if detection['top_right']:
                serials.append(int(buffer[0][index + 1:index + 4].strip('.')))
        elif not detection['top_left']:
            serials.append(int(buffer[0][index:index + 3].strip('.')))
        elif not detection['top_right']:
            serials.append(int(buffer[0][index - 2:index + 1].strip('.')))

    # read the middle row for detections
    if detection['left']:
        serials.append(int(buffer[1][index - 3:index].strip('.')))
    if detection['right']:
        serials.append(int(buffer[1][index + 1:index + 4].strip('.')))

    # read the bottom row for detections
    if detection['bottom_left'] or detection['bottom'] or detection['bottom_right']:
        if detection['bottom'] and detection['bottom_left'] and detection['bottom_right']:
            serials.append(int(buffer[2][index - 1:index + 2].strip('.')))
        elif not detection['bottom']:
            if detection['bottom_left']:
                serials.append(int(buffer[2][index - 3:index].strip('.')))
            if detection['bottom_right']:
                serials.append(int(buffer[2][index + 1:index + 4].strip('.')))
        elif not detection['bottom_left']:
            serials.append(int(buffer[2][index:index + 3].strip('.')))
        elif not detection['bottom_right']:
            serials.append(int(buffer[2][index - 2:index + 1].strip('.')))
    if len(serials) == 2:
        return mul(serials[0], serials[1])
    else:
        return 0


with open('input.txt', 'r') as file:
    content = file.read().splitlines()
    # this is the buffer of the lines to be held in memory during execution
    line_buffer = deque(([], [], []), maxlen=3)
    for line in content:
        line_buffer.append(line)
        sum_of_numbers = find_serial_numbers(line_buffer)
        if sum_of_numbers:
            final_result += sum_of_numbers
    line_buffer.append([])
    sum_of_numbers = find_serial_numbers(line_buffer)
    if sum_of_numbers:
        final_result += sum_of_numbers
    print(final_result)