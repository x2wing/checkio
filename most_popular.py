def popular_words_my(text: str, words: list) -> dict:
    # find frequency of finding out same word in text
    frequency = {}
    text = text.lower().split()
    for word in words:
        frequency[word] = text.count(word)
    return frequency


def popular_words(text: str, words: list) -> dict:

    return {word: text.lower().split().count(word) for word in words}



if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
