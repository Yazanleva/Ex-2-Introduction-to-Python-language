# S3_LAM_03 — Closure factory (make_adder)

def make_adder(x):
    return lambda y: x + y

add10 = make_adder(10)
add3 = make_adder(3)

print(add10(5))  # 15
print(add3(5))   # 8
