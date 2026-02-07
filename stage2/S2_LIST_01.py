# S2_LIST_01 — Clean number strings

def clean_numbers(values):
    out = []
    for s in values:
        try:
            num = float(str(s).strip())
            out.append(num)
        except Exception:
            pass
    return out


# Tests
print(clean_numbers([" 1 ", "x", "2"]))         # [1.0, 2.0]
print(clean_numbers(["3.5", "  -2 ", "nope"]))  # [3.5, -2.0]

