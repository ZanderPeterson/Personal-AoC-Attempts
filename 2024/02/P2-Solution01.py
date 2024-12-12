from typing import List

input_file: str = "input.txt"

#Get the data, and put into two arrays.
safe_reports: int = 0
with open (input_file, "r") as file:
    for report in file:
        #Get Report Data into an Array of Integers
        report_str: List[str] = report.split(' ')
        report_int: List[int] = []
        for value in report_str:
            if value == " ":
                continue #For some reason I haven't figured out, split kept the spaces.
            report_int.append(int(value))

        for i in range(len(report_int) + 1):
            dampened_report_attempt: List[int] = report_int.copy()

            if i != 0:
                dampened_report_attempt.pop(i - 1)
            report_ascending_safely: bool = True
            report_descending_safely: bool = True

            previous_value: int = dampened_report_attempt[0]
            for value in dampened_report_attempt[1:]:
                if 3 < (value - previous_value) or 1 > (value - previous_value):
                    report_ascending_safely = False
                    break
                previous_value = value

            previous_value: int = dampened_report_attempt[0]
            for value in dampened_report_attempt[1:]:
                if 3 < (previous_value - value) or 1 > (previous_value - value):
                    report_descending_safely = False
                    break
                previous_value = value

            if report_ascending_safely or report_descending_safely:
                safe_reports += 1
                break

print(f"The Calculated Answer to AoC 2024-02 Part 2 for the provided '{input_file}' data set is: {safe_reports}")
