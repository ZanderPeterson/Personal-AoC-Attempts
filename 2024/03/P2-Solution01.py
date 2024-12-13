from typing import List

input_file: str = "input.txt"

#Get Data
with open (input_file, "r") as memory:
    corrupted_memory: str = memory.read()

do_mul: bool = True #True if do(), False if don't()
answer: int = 0
mul_location: int = corrupted_memory.find("mul(")
do_location: int = corrupted_memory.find("do()")
dont_location: int = corrupted_memory.find("don't()")

while mul_location != -1: #While a 'mul(' has been found

    if do_location != -1 and (do_location < dont_location or dont_location == -1) and do_location < mul_location:
        corrupted_memory = corrupted_memory[do_location + len("do()"):]
        do_mul = True
        mul_location = corrupted_memory.find("mul(")
        do_location = corrupted_memory.find("do()")
        dont_location = corrupted_memory.find("don't()")
        continue

    if dont_location != -1 and (dont_location < do_location or do_location == -1) and dont_location < mul_location:
        corrupted_memory = corrupted_memory[dont_location + len("don't()"):]
        do_mul = False
        mul_location = corrupted_memory.find("mul(")
        do_location = corrupted_memory.find("do()")
        dont_location = corrupted_memory.find("don't()")
        continue

    corrupted_memory = corrupted_memory[mul_location + len("mul("):] #Remove all characters before first instance of 'mul(', including 'mul('

    if not do_mul:
        mul_location = corrupted_memory.find("mul(")
        do_location = corrupted_memory.find("do()")
        dont_location = corrupted_memory.find("don't()")
        continue

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
    do_location = corrupted_memory.find("do()")
    dont_location = corrupted_memory.find("don't()")

print(f"The Calculated Answer to AoC 2024-03 Part 2 for the provided '{input_file}' data set is: {answer}")
