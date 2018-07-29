def between_markers1(text: str, begin: str, end: str) -> str:
    b = text.find(begin)
    e = text.find(end)
    # if begin and end aren't found return all input text
    if b < 0  and e < 0:
        return text
    elif e > 0 and b > e:
        return ""
        
    b = 0 if b < 0 else b+len(begin)
    e = len(text) if e < 0 else e
         
    return text[b:e]



def between_markers (text, m1, m2):

    return text[text.find(m1) + 
    (1 if text.find(m1) == -1 else len(m1)):len(text)  if text.find(m2) == -1 else text.find(m2)]

    


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')