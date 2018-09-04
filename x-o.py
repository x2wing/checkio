from typing import List
import numpy as np

def checkio(game_result: List[str]) -> str:
    a = np.array(list(''.join(game_result)), str).reshape(3,3)
    result = list(filter(lambda M:  M[0] != '.' and np.all(M[1:] == M[:-1]), list(a) + list(a.T) + list(np.diag(np.fliplr(a)).reshape(1,3)) + list(np.diag(a).reshape(1,3))  ))
    return result[0][0] if result!=[]  else 'D'

if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")