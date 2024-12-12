from typing import List

input_file: str = "input.txt"

#Get the data, and put into a large array.
list_a: List[int] = []
list_b: List[int] = []
with open (input_file, "r") as file:
    for line in file:
        list_a.append(int(line.split()[0]))
        list_b.append(int(line.split()[1]))

#Iterate over the data, run calculations
answer: int = 0
for location_id in list_a:
    same_id = list_b.count(location_id)
    answer += location_id * same_id

print(f"The Calculated Answer to AoC 2024-01 Part 2 for the provided '{input_file}' data set is: {answer}")
