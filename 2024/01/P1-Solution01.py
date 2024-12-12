from typing import List

input_file: str = "input.txt"

#Get the data, and put into two arrays.
list_a: List[int] = []
list_b: List[int] = []
with open (input_file, "r") as file:
    for line in file:
        list_a.append(int(line.split()[0]))
        list_b.append(int(line.split()[1]))

#Sort the respective data sets
list_a = sorted(list_a)
list_b = sorted(list_b)
sorted_data: List[int] = []
for i in range(len(list_a)):
    sorted_data.append(list_a[i])
    sorted_data.append(list_b[i])

#Iterate over the pairs of data, run calculations
answer: int = 0
for i in range(len(sorted_data)//2):
    num1: int = sorted_data[i*2] #2i + 2 - 2 = 2i
    num2: int = sorted_data[i*2 + 1] # 2i + 2 - 1 = 2i + 1
    distance: int = abs(num1 - num2)
    answer += distance

print(f"The Calculated Answer to AoC 2024-01 Part 1 for the provided '{input_file}' data set is: {answer}")
