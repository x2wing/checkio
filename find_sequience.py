import numpy as np
from pprint import pprint

dimension = 4


def match_sequence(L: list) -> bool:
    counter = 1
    for i in range(1, L.__len__()):
        if L[i - 1] == L[i]:
            counter += 1
            if counter == dimension:
                return True
        else:
            counter = 1


def checkio(M):
    M = np.array(M)
    for i in range(M.__len__()):
        if match_sequence(M[i]): return True  # is match sequence in row
        if match_sequence(M[:, i]): return True  # is match sequence in col
        # print(a.diagonal())
    for i in range(dimension - len(M), len(M) - dimension + 1):
        if match_sequence(M.diagonal(i)): return True
        if match_sequence((np.fliplr(M)).diagonal(i)): return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
