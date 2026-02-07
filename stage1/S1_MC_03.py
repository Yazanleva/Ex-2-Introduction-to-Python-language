# S1_MC_03 — Simple calculator (match/case)

def calc(a, op, b):
    # validate numbers
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return None

    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b == 0:
                return None
            return a / b
        case _:
            return None


# Tests
tests = [
    (1, "+", 2),
    (5, "-", 3),
    (2, "*", 4),
    (10, "/", 2),
    (10, "/", 0),
    (1, "%", 2),
]

for t in tests:
    print(t, "->", calc(*t))
