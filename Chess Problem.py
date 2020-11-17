from math import *

num_of_testcase = int(input())
total_testcase = num_of_testcase

nums = []

while num_of_testcase != 0:
    nums.append(input())
    num_of_testcase -= 1

board = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    5: "E",
    6: "F",
    7: "G",
    8: "H",

}


def is_possible(lists):
    output = []
    for value in lists:
        first = int(value[2])
        second = int(value[6])
        if value[0] == value[4] and value[2] == value[6]:
            output.append("0 " + value[0: 3])
        elif abs(ord(value[0]) - ord(value[4])) == abs(first - second):
            output.append("1 " + value)
        elif value[0] == value[4] and ((max(first, second) % min(first, second)) % 2) == 1:
            output.append("Impossible")
        elif abs(ord(value[0]) - ord(value[5])) % 2 == 1 and ((max(first, second) % min(first, second)) % 2) == 1:
            output.append("Impossible")
        else:
            move1 = floor((max(first, second) - min(first, second)) / 2)
            move2 = (max(first, second) - min(first, second)) - move1
            if board.get(value[0]) - move2 > 0: #Moves left
                if first + move2 < 8: #Moves up
                    output.append(
                        "2 " + value[0: 3] + " " + board.get(board.get(value[0]) - move2) + " " + str(
                            move2 + int(value[2])) + " " + value[4:])
                else: #Moves down
                    output.append(
                        "2 " + value[0: 3] + " " + board.get(board.get(value[0]) - move1) + " " + str(
                            -move1 + int(value[2])) + " " + value[4:])
            else: # Move right
                if first + move2 < 8:  # Moves up
                    output.append(
                        "2 " + value[0: 3] + " " + board.get(board.get(value[0]) + move2) + " " + str(
                            move2 + int(value[2])) + " " + value[4:])
                else:  # Moves down
                    output.append(
                        "2 " + value[0: 3] + " " + board.get(board.get(value[0]) + move1) + " " + str(
                            -move1 + int(value[2])) + " " + value[4:])

    return output


for lists in is_possible(nums):
    print(lists)
