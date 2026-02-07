# S1_IF_03 — Normalize user name

def normalize_name(x):
    if not x:
        return "Anonymous"

    s = str(x).strip()
    if s == "":
        return "Anonymous"

    return s


# Tests (exactly as requested)
tests = ["", " ", None, " Ola "]

for t in tests:
    print(repr(t), "->", normalize_name(t))
