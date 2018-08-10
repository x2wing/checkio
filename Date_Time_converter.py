# print(tmp_form_of_time.strftime('%#d %B %Y year %#H hours %#M minutes'))
# print(f'{tmp_form_of_time:%#H}')
from datetime import datetime
def date_time(time: str) -> str:
    tmp_form_of_time = datetime.strptime(time, "%d.%m.%Y %H:%M")
    hour = 'hour' if f'{tmp_form_of_time:%#H}' == '1' else 'hours'
    minute = 'minute' if f'{tmp_form_of_time:%#M}' == '1' else 'minutes'
    return tmp_form_of_time.strftime(f'%#d %B %Y year %#H {hour} %#M {minute}')

if __name__ == '__main__':
    # print("Example:")
    # print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")