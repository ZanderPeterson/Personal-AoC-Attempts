from typing import Dict, List

input_file: str = "inputs/input.txt"

answer: int = 0

#Get Data
with open (input_file, "r") as input_data:
    rules: Dict[int, List[int]] = {}
    for line in input_data:
        if "|" in line:
            #Line defines a rule
            num1: int = int(f"{line[0]}{line[1]}")
            num2: int = int(f"{line[3]}{line[4]}")
            if num1 in rules.keys():
                rules[num1].append(num2)
            else:
                rules[num1] = [num2]
            continue

        if len(line) == 1:
            continue

        book: List[int] = []
        for i in range(len(line)//3):
            violation: bool = False
            new_page_number: int = int(f"{line[i*3]}{line[i*3 + 1]}")
            for page_number in book:
                if page_number in rules[new_page_number]:
                    violation = True
                    break
            book.append(new_page_number)
            if violation:
                break
        else:
            #Page order is good
            answer += book[len(book)//2]

print(f"The Calculated Answer to AoC 2024-05 Part 1 for the provided '{input_file}' data set is: {answer}")
