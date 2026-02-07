def is_truthy(v):
    return bool(v)

tests = [0, 1, "", "0", [], [0], {}, None]

for t in tests:
    print(t, "->", is_truthy(t))
