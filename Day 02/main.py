# Advent of Code 2023 - Day 2 Solution

# initialize final sum
final_result = 0

# iterate though the draws and determine the minimum number of each color needed
def read_contents(draws):
    total_red, total_green, total_blue = 0, 0, 0
    for draw in draws:
        draw = draw.split(',')
        red, green, blue = 0, 0, 0
        for count in draw:
            if count.endswith('red'):
                count = count.rstrip('red').strip()
                red = int(count)
                if red > total_red:
                    total_red = red
            elif count.endswith('green'):
                count = count.rstrip('green').strip()
                green = int(count)
                if green > total_green:
                    total_green = green
            elif count.endswith('blue'):
                count = count.rstrip('blue').strip()
                blue = int(count)
                if blue > total_blue:
                    total_blue = blue
    # multiplies all totals and returns the result
    multiplied = total_red * total_green * total_blue
    return multiplied


with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip('Game ').strip('\n').partition(':')
        game_id = int(line[0])
        contents = read_contents(line[2].split(';'))
        final_result = final_result + contents
    print(f'final result: {final_result}')