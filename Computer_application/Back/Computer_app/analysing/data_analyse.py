import sys

sys.path.append('')


def leap_year(year):
    year = int(year)
    if (year % 4 == 0 or year % 400 == 0) and year % 100 != 0:
        return True
    return False


def check_on_right_date(date):
    data = preparation(date)
    date_to_work = date.split('.')
    my_dict = {'01': 31, '02': 28, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31, '08': 31, '09': 30, '10': 31,
               '11': 30, '12': 31}
    my_dict2 = {'01': 31, '02': 29, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31, '08': 31, '09': 30, '10': 31,
                '11': 30, '12': 31}
    if len(date_to_work[0]) == 2:
        if len(date_to_work[1]) == 2:
            if len(date_to_work[2]) == 4:
                if leap_year(date_to_work[2]):
                    if (int(my_dict2[date_to_work[1]]) >= int(date_to_work[0]) > 0) and 0 < int(date_to_work[1]) < 13:
                        return True
                else:
                    if (int(my_dict[date_to_work[1]]) >= int(date_to_work[0]) > 0) and 0 < int(date_to_work[1]) < 13:
                        return True
    return False


def preparation(data):
    if data.isalnum() == False:
        data2 = ''
        for i in data:
            if i.isdigit():
                data2 += i
            else:
                data2 += '.'
        data = data2.split('.')
        if len(data[0]) == 2 and len(data[1]) == 2 and len(data[2]) == 4:
            data = '.'.join(data)
        elif len(data[0]) == 4 and len(data[1]) == 2 and len(data[2]) == 2:
            data = data[::-1]
            data = '.'.join(data)
        else:
            return None
        return data

    return None


if __name__ == '__main__':
    assert preparation('16.02.2011') == '16.02.2011'
    assert preparation('2011.02.16') == '16.02.2011'
    assert preparation('a') == None
    assert preparation('16-02-2011') == '16.02.2011'
    assert preparation('16,02,2011') == '16.02.2011'
    assert preparation('2011,02,16') == '16.02.2011'
    assert preparation('***') == None
    assert preparation('000') == None
    assert check_on_right_date('16.02.2011') == True
    # assert check_on_right_date('00.01.2023') == 
    # assert check_on_right_date('') == 
    # assert check_on_right_date('') == 
    # assert check_on_right_date('') == 
    # assert check_on_right_date('') == 
    # assert check_on_right_date('') == 
    # assert check_on_right_date('') == 
    # assert check_on_right_date('') ==
