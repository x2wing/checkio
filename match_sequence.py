def match_sequence(L: list) -> bool:
    counter = 1
    for i in range(1, L.__len__()):
        if L[i - 1] == L[i]:
            counter += 1
            if counter == 4:
                return True
        else:
            counter = 1

    return False


print(match_sequence([5,5,5, 4,4,4, 40,53, 3, 3, 4, 4, 4,6,6,7,8]))
