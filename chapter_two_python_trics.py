#!/usr/local/bin/python3

test = '''
We spend several years building our own database engine,
Amazon Aurora, a fully-managed MySQL and PostgreSQL-competible
servise with the same or better durability and availavility as
the commercial engines, byt at one-tenth of the cost.
'''

test['turs':'name'] = 'name turs turs name'
print(test)


price = [[9.9, 9.8, 9.8, 9.6, 9.4],
         [9.5, 9.4, 9.3, 9.3, 9.2]]


print([value[::2] for value in price])
