from typing import Dict, List

input_file: str = "inputs/input.txt"

def print_array(array_to_print: List[list]) -> None:
    print("-"*len(array_to_print[0]*5))
    for row in array_to_print:
        print(row)
    print("-" * len(array_to_print[-1])*5)

answer: int = 0

#Get Data
with open (input_file, "r") as input_data:
    lab_map: List[List[str]] = []
    for line in input_data:
        lab_map.append(list(line[:-1]))

#print_array(lab_map)

guard_position: List[int] = [0, 0]
for i in range(len(lab_map)):
    for j in range(len(lab_map[0])):
        if lab_map[i][j] in ["^", ">", "v", "<"]:
            guard_position = [j, i]
            break
    if guard_position != [0, 0]:
        break

while ((guard_position[0] >= 0) and
       (guard_position[1] >= 0) and
       (guard_position[0] <= len(lab_map[0]) - 1) and
       (guard_position[1] <= len(lab_map) - 1)):
    current_tile: str = lab_map[guard_position[1]][guard_position[0]]
    next_tile: List[int] = []
    if current_tile == "^":
        next_tile = [guard_position[0] + 0, guard_position[1] - 1]
    elif current_tile == ">":
        next_tile = [guard_position[0] + 1, guard_position[1] + 0]
    elif current_tile == "v":
        next_tile = [guard_position[0] + 0, guard_position[1] + 1]
    elif current_tile == "<":
        next_tile = [guard_position[0] - 1, guard_position[1] + 0]

    try:
        if lab_map[next_tile[1]][next_tile[0]] == "#":
            if current_tile == "^":
                lab_map[guard_position[1]][guard_position[0]] = ">"
            elif current_tile == ">":
                lab_map[guard_position[1]][guard_position[0]] = "v"
            elif current_tile == "v":
                lab_map[guard_position[1]][guard_position[0]] = "<"
            elif current_tile == "<":
                lab_map[guard_position[1]][guard_position[0]] = "^"
        else:
            lab_map[guard_position[1]][guard_position[0]] = "X"
            lab_map[next_tile[1]][next_tile[0]] = current_tile
            guard_position = next_tile
    except IndexError:
        lab_map[guard_position[1]][guard_position[0]] = "X"
        break
    #print(guard_position)
    #print_array(lab_map)

#print_array(lab_map)
#print(guard_position)

for i in range(len(lab_map)):
    for j in range(len(lab_map[0])):
        if lab_map[i][j] == "X":
            answer += 1



print(f"The Calculated Answer to AoC 2024-06 Part 1 for the provided '{input_file}' data set is: {answer}")
