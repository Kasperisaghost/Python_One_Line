
from timeit import timeit
from enum import Enum


customers = [('John', 200_000), ('Alice', 100)]

whales = [name for name, _ in customers if _ > 100_000]
print(whales)
