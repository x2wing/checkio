is_polindrom = lambda text: text == text[::-1]


def longest_palindromic(text):
    return max([
                   text[i:j] + text[i:j - 1][::-1]
                   for i in range(len(text) - 1)
                   for j in range(i + 1, i + 2 + int(len(text) / 2))
                   if (text[i:j] + text[i:j - 1][::-1]) in text
               ] or [text], key=len)


def longest_palindromic_my(text):
    max = 0
    for i in range(0, text.__len__()):
        for j in range(i + 1, text.__len__() + 1):
            str = text[i:j]
            if is_polindrom(str):
                if len(str) > max:
                    max = len(str)
                    max_str = str
    return max_str


print(f'Polindrome = {text[i:j]} len = {len(text[i:j])}')

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
