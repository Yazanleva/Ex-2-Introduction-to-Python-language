def eq(actual, expected):
    if actual != expected:
        raise AssertionError(f"{actual} != {expected}")
