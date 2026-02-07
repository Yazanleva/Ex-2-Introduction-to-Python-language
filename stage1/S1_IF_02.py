# S1_IF_02 — Score to grade

def grade(score):
    if not isinstance(score, (int, float)) or score < 0 or score > 100:
        return None

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# Boundary tests
tests = [59, 60, 69, 70, 89, 90, 100, 101]

for t in tests:
    print(t, "->", grade(t))
