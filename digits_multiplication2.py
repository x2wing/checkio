from functools import reduce
def checkio(whole: int) -> int:
    mul = 1
    while whole > 0:
        whole, reminder = divmod(whole, 10)
        if reminder: mul*=reminder 
    return mul
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
