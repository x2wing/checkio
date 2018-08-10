def non_repeat1(line):
    """

        the longest substring without repeating chars

    """

    if not line:
        return line
    line_len = len(line)
    for slice_len in range(line_len, 0, -1):
        for i in range(line_len - slice_len + 1):
            slice_ = line[i:i + slice_len]
            if len(slice_) == len(set(slice_)):
                return slice_


import re

import itertools


def non_repeat(line):
    return line if len(line) < 2 else max(
        [line[d[0]:d[1]] if not re.search(r"(.).*\1", line[d[0]:d[1]]) else "" for d in
         itertools.product(range(len(line)), range(len(line) + 1))], key=lambda s: len(s))


def non_repeat_old(line):
    r = []
    for i in range(len(line)):
        for j in range(i, len(line) + 1):
            if not re.search(r"(.).*\1", line[i:j]):
                r.append(line[i:j])

    return line if len(line) < 2 else max(r, key=lambda s: len(s))


def non_repeat(line):
    unique = []
    for i in range(len(line)):
        unique.append([])
        for char in line[i:]:
            if char not in unique[i]:
                unique[i].append(char)
            else:
                break
    return ''.join(max(unique, key=len))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    assert non_repeat('aaaaa') == 'a', "First"

    assert non_repeat('abdjwawk') == 'abdjw', "Second"

    assert non_repeat('abcabcffab') == 'abcf', "Third"

    print('"Run" is good. How is "Check"?')
