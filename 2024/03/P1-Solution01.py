from typing import List

input_file: str = "input.txt"

#Get Data
with open (input_file, "r") as memory:
    corrupted_memory: str = memory.read()

answer: int = 0
mul_location: int = corrupted_memory.find("mul(")
while mul_location != -1: #While a 'mul(' has been found
    corrupted_memory = corrupted_memory[mul_location+4:] #Remove all characters before first instance of 'mul(', including 'mul('

    on_first_number: bool = True
    on_second_number: bool = False
    finished_expression: bool = False
    error_found: bool = False

    num1_str: str = ""
    accepted_digits: List[str] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while on_first_number and (not error_found):
        if corrupted_memory[0] in accepted_digits:
            num1_str = f"{num1_str}{corrupted_memory[0]}"
        elif corrupted_memory[0] == ",":
            on_first_number = False
            on_second_number = True
        else:
            error_found = True
        corrupted_memory = corrupted_memory[1:]

    num2_str: str = ""
    while on_second_number and (not error_found) and (not finished_expression):
        if corrupted_memory[0] in accepted_digits:
            num2_str = f"{num2_str}{corrupted_memory[0]}"
        elif corrupted_memory[0] == ")":
            on_second_number = False
            finished_expression = True
        else:
            error_found = True
        corrupted_memory = corrupted_memory[1:]

    if (not error_found) and finished_expression and (3 >= len(num1_str) >= 1) and (3 >= len(num2_str) >= 1):
        answer += int(num1_str) * int(num2_str)

    mul_location = corrupted_memory.find("mul(")

print(f"The Calculated Answer to AoC 2024-03 Part 1 for the provided '{input_file}' data set is: {answer}")
