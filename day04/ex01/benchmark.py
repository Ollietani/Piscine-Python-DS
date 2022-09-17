#!/usr/bin/env python3
import timeit


def emails_data():
    emails = ['john@gmail.com', 'james@gmail.com',
              'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    return emails * 5


def list_comprehension():
    emails = emails_data()
    return [x for x in emails if x.partition('@')[2] == 'gmail.com']


def map_function():
    emails = emails_data()
    return list(map(lambda x: x if x.partition('@')[2] == 'gmail.com' else None, emails))


def loop():
    emails = emails_data()
    result = []
    for data in emails:
        if data.partition('@')[2] == 'gmail.com':
            result.append(data)
    return result


def compare_functions():
    time = 90_000_0
    res = {'comp': timeit.timeit("list_comprehension()", setup="from __main__ import list_comprehension", number=time),
           'loop': timeit.timeit("loop()", setup="from __main__ import loop", number=time),
           'map': timeit.timeit("map_function()", setup="from __main__ import map_function", number=time)
           }
    data = sorted(res.items(), key=lambda item: item[1])
    if data[0][0] == 'comp':
        print('it is better to use a list comprehension')
    elif data[0][0] == 'loop':
        print('it is better to use a loop')
    else:
        print('it is better to use a map')
    print(data[0][1], 'vs', data[1][1], 'vs', data[2][1])


if __name__ == '__main__':
    compare_functions()