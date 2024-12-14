from typing import List

input_file: str = "input.txt"

def count_words(str1: str, str2: str) -> int:
    """Counts the number of instances of str2 in str1, and returns that value."""
    instances: int = 0
    str2_location: int = str1.find(str2)
    while str2_location != -1:
        str1 = str1[str2_location + len(str2):]
        str2_location: int = str1.find(str2)
        instances += 1
    return instances

def list_to_str(list_to_convert: List[str], reverse: bool = False) -> str:
    """
    Converts a list of strings into one large string.
    E.g. ["a", "b", "cd"] -> "abcd"
    And can even make it reversed.
    E.g. ["a", "b", "cd"] -> "cdab"
    """
    return_string: str = ""
    if reverse:
        for element in list_to_convert:
            return_string = f"{element}{return_string}"
    else:
        for element in list_to_convert:
            return_string = f"{return_string}{element}"
    return return_string

#Get Data
with open (input_file, "r") as word_search_file:
    word_search: List[List[str]] = []
    for line in word_search_file:
        word_search.append(list(line[:-1])) #Removes '\n' from line, turns string into list, and adds it to data.

#print(word_search)

answer: int = 0

#Horizontal Lines
for horizontal_line in word_search:
    answer += count_words(list_to_str(horizontal_line, reverse=False), "XMAS")
    answer += count_words(list_to_str(horizontal_line, reverse=True), "XMAS")
print(f"Horizontal Lines: {answer}")

#Vertical Lines
for i in range(len(word_search[0])):
    list_to_check: List[str] = []
    for j in range(len(word_search)):
        list_to_check.append(word_search[j][i])

    answer += count_words(list_to_str(list_to_check, reverse=False), "XMAS")
    answer += count_words(list_to_str(list_to_check, reverse=True), "XMAS")
print(f"Vertical Lines: {answer}")

#Diagonal Lines |\
for i in range(len(word_search)):
    list_to_check: List[str] = []
    x_position: int = 0
    y_position: int = i
    while x_position < len(word_search[0]) and y_position < len(word_search):
        list_to_check.append(word_search[y_position][x_position])
        x_position += 1
        y_position += 1
    answer += count_words(list_to_str(list_to_check, reverse=False), "XMAS")
    answer += count_words(list_to_str(list_to_check, reverse=True), "XMAS")
print(f"Diagonal Lines: {answer}")

#Diagonal Lines _\
for i in range(len(word_search[0])):
    list_to_check: List[str] = []
    x_position: int = i + 1
    y_position: int = 0
    while x_position < len(word_search[0]) and y_position < len(word_search):
        list_to_check.append(word_search[y_position][x_position])
        x_position += 1
        y_position += 1
    answer += count_words(list_to_str(list_to_check, reverse=False), "XMAS")
    answer += count_words(list_to_str(list_to_check, reverse=True), "XMAS")
print(f"Diagonal Lines: {answer}")

#Diagonal Lines |/
for i in range(len(word_search)):
    list_to_check: List[str] = []
    x_position: int = 0
    y_position: int = i
    while x_position < len(word_search[0]) and y_position < len(word_search):
        list_to_check.append(word_search[y_position][-x_position - 1])
        x_position += 1
        y_position += 1
        #print(f"{x_position}, {y_position}")
    answer += count_words(list_to_str(list_to_check, reverse=False), "XMAS")
    answer += count_words(list_to_str(list_to_check, reverse=True), "XMAS")
print(f"Diagonal Lines: {answer}")

#Diagonal Lines _/
for i in range(len(word_search[0])):
    list_to_check: List[str] = []
    x_position: int = i + 1
    y_position: int = 0
    while x_position < len(word_search[0]) and y_position < len(word_search):
        list_to_check.append(word_search[y_position][-x_position - 1])
        x_position += 1
        y_position += 1
        #print(f"{x_position}, {y_position}")
    answer += count_words(list_to_str(list_to_check, reverse=False), "XMAS")
    answer += count_words(list_to_str(list_to_check, reverse=True), "XMAS")
print(f"Diagonal Lines: {answer}")

print(f"The Calculated Answer to AoC 2024-04 Part 1 for the provided '{input_file}' data set is: {answer}")
