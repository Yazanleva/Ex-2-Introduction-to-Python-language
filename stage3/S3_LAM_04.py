# S3_LAM_04 — Sum of squares of even numbers

from functools import reduce

nums = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda n: n % 2 == 0, nums))
squares = list(map(lambda n: n * n, evens))
total = reduce(lambda a, b: a + b, squares, 0)

print("nums:", nums)
print("evens:", evens)
print("squares:", squares)
print("sum:", total)  # 2^2 + 4^2 + 6^2 = 56
