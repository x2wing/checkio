def time_converter(time):
    time, sun = time.split()
    hours, minutes = time.split(':')
    if sun == "p.m." and hours != '12': hours = str(int(hours) + 12)
    elif time == "12:00" and sun == "p.m.":
        return time
    elif time == "12:00" and sun == "a.m.":
        return '00:00'
    if len(hours) == 1:  hours = '0' + hours
    print(f'{hours}:{minutes}')
    return f'{hours}:{minutes}'


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30 p.m.'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    assert time_converter('12:00 p.m.') == '12:00'
    print("Coding complete? Click 'Check' to earn cool rewards!")
