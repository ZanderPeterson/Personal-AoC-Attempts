from typing import List

input_file: str = "input.txt"

#Get Data
with open (input_file, "r") as memory:
    wordsearch: str = memory.read()

print(f"The Calculated Answer to AoC 2024-03 Part 1 for the provided '{input_file}' data set is: {"None"}")
