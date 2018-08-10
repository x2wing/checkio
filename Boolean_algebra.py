def boolean(x, y, operation):
    return {
        "conjunction": lambda x, y: x & y,
        "disjunction": lambda x, y: x | y,
        "implication": lambda x, y: not x or y,
        "exclusive": lambda x, y: x ^ y,
        "equivalence": lambda x, y: x == y,
    }[operation](x, y)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
