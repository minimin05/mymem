# matrix = [
#     [1, 2, 3],
#     [4, 5, 6], 
# ]
# matrix[0][1] = 10
# for row in matrix:
#     for element in row:
#         print(element, end=' ')
#     print()

import random

ROWS = 3
COLS = 4

def main():
    value = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    for r in range(ROWS):
        for c in range(COLS):
            value[r][c] = random.randint(1, 100)
    print(value)

main()