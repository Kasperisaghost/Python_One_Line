#!/usr/local/bin/python3
from timeit import timeit


print(timeit('[(value.strip(), "anonymus" in value) for value in open("test.txt")]', number=10_000))
print(timeit('map(lambda s: (s, True) if "anonymus" in s else (s, False), open("test.txt"))', number=10_000))




