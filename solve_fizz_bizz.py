def checkio_my(n: int) -> str:
    return ['Fizz Buzz', "Buzz", "Fizz", str(n)][0 if not n%15 else (1 if not n%5 else (2 if not n%3 else 3))] 



def checkio(number: int) -> str:

    # Your code here

    # It's main function. Don't remove this function

    # It's using for auto-testing and must return a result for check.

    return max(str(number),'Fizz '*(number % 3 == 0)+'Buzz'*(number % 5 == 0)).strip()


# Some hints:
# Convert a number in the string with str(n)

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(9999150000000000000000000) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
