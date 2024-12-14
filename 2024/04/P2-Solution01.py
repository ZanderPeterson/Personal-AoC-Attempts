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

def search_for_x_mas(grid: List[List[str]]) -> bool:
    if grid[1][1] != "A":
        return False
    return (((grid[0][0] == "M" and grid[2][2] == "S") or (grid[0][0] == "S" and grid[2][2] == "M")) and
            ((grid[2][0] == "M" and grid[0][2] == "S") or (grid[2][0] == "S" and grid[0][2] == "M")))

#Get Data
with open (input_file, "r") as word_search_file:
    word_search: List[List[str]] = []
    for line in word_search_file:
        word_search.append(list(line[:-1])) #Removes '\n' from line, turns string into list, and adds it to data.

#print(word_search)

answer: int = 0
for x in range(len(word_search[0]) - 2):
    for y in range(len(word_search) - 2):
        search_area: List[List[str]] = [[word_search[y + 0][x + 0], word_search[y + 0][x + 1], word_search[y + 0][x + 2]],
                                        [word_search[y + 1][x + 0], word_search[y + 1][x + 1], word_search[y + 1][x + 2]],
                                        [word_search[y + 2][x + 0], word_search[y + 2][x + 1], word_search[y + 2][x + 2]],]
        #print(search_area)
        if search_for_x_mas(search_area):
            answer += 1

print(f"The Calculated Answer to AoC 2024-04 Part 2 for the provided '{input_file}' data set is: {answer}")
