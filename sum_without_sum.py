# nakopitel = 0
# counter = 0
# def foo(element):
#     global nakopitel, counter
#     nakopitel += element
#     if counter = len[L]
#     return  nakopitel


def checkio(L: list) -> int:
    if len(L) <= 0:
        return 0
    else:
        return L.pop() + checkio(L)


checkio([1, 2, 3]) == 6

checkio([2, 2, 2, 2, 2, 2]) == 12
