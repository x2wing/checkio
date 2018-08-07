def largest_histogram(hist):
    mas_square = []
    l = hist.__len__()
    for i in range(0, l):
        for j in range(i + 1, l + 1):
            s = hist[i:j]
            mas_square.append(min(s) * len(s))
    return max(mas_square)


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert largest_histogram([5]) == 5, "one is always the biggest"
    # assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")
