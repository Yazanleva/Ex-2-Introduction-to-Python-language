# S3_PIPE_04 — Iterable pipeline (generator-based)

def strip_all(items):
    for s in items:
        yield str(s).strip()

def to_float_skip(items):
    for s in items:
        try:
            yield float(s)
        except Exception:
            continue

def double_all(items):
    for n in items:
        yield n * 2

def sum_all(items):
    total = 0.0
    for n in items:
        total += n
    return total

values = [" 1 ", "x", " 2.5 ", "nope", "3"]

pipeline = double_all(to_float_skip(strip_all(values)))
result = sum_all(pipeline)

print(result)  # (1 + 2.5 + 3) * 2 = 13.0
