# S3_PIPE_06 — Safe pipeline (pipe_safe)

def pipe_safe(*fns):
    def run(x):
        try:
            for fn in fns:
                x = fn(x)
            return {"ok": True, "value": x}
        except Exception as e:
            return {"ok": False, "error": str(e)}
    return run


# Tests
def to_int(s):
    s = str(s).strip()
    if s == "" or any(ch.isalpha() for ch in s):
        raise ValueError("bad int input")
    return int(s)

def half(n):
    if n == 0:
        raise ValueError("cannot half zero")
    return n / 2

safe = pipe_safe(to_int, half)

print(safe("10"))  # ok True, value 5.0
print(safe("x"))   # ok False
print(safe("0"))   # ok False
