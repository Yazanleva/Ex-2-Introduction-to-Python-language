# S3_LAM_01 — Convert to lambdas

square = lambda n: n * n
is_odd = lambda n: n % 2 != 0
greet = lambda name: f"Hello, {name}!"

# 3 tests per lambda
print(square(2), square(5), square(-3))
print(is_odd(1), is_odd(2), is_odd(9))
print(greet("Ola"), greet("Eva"), greet("Adam"))
