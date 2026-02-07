# S2_FOR_01 — FizzBuzz+ (1..30)

for i in range(1, 31):
    fizz = (i % 3 == 0)
    buzz = (i % 5 == 0)

    if fizz and buzz:
        print("FizzBuzz")
    elif fizz:
        print("Fizz")
    elif buzz:
        print("Buzz")
    else:
        print(i)
