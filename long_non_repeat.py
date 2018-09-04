from pprint import pprint


def non_repeat(line):
    max = 0
    for i in range(0, line.__len__()):
        substr = line[i]
        for j in range(i + 1, line.__len__()):
            if line[j] in substr:
                break
            else:
                substr += line[j]
        if len(substr) > max:
            max = len(substr)
            max_str = substr
    return max_str



if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    print('"Run" is good. How is "Check"?')
