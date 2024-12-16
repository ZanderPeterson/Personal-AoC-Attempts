from typing import Dict, List

input_file: str = "inputs/example_input_p1"

answer: int = 0

#Get Data
with open (input_file, "r") as input_data:
    rules: Dict[int, List[int]] = {}
    for line in input_data:
        pass

print(f"The Calculated Answer to AoC 2024-06 Part 1 for the provided '{input_file}' data set is: {answer}")
