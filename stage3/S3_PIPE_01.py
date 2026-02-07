# S3_PIPE_01 — pipe(*fns) left-to-right (unary)

def pipe(*fns):
    def run(x):
        for fn in fns:
            x = fn(x)
        return x
    return run

# Tests (numeric transforms)
add1 = lambda x: x + 1
double = lambda x: x * 2

f = pipe(add1, double)   # (x+1) then *2
print(f(3))  # 8
