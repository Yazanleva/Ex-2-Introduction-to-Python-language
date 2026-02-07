import math

nan1 = float("nan")

try:
    nan2 = 0.0 / 0.0
except ZeroDivisionError:
    nan2 = float("nan")

print(nan1 == nan1)
print(math.isnan(nan1))
print(math.isnan(nan2))
