# S3_PIPE_02 — compose(*fns) right-to-left

def pipe(*fns):
    def run(x):
        for fn in fns:
            x = fn(x)
        return x
    return run

def compose(*fns):
    def run(x):
        for fn in reversed(fns):
            x = fn(x)
        return x
    return run

add1 = lambda x: x + 1
double = lambda x: x * 2

p = pipe(add1, double)       # (x+1)*2
c = compose(add1, double)    # add1(double(x)) = 2x+1

print("pipe:", p(3))     # 8
print("compose:", c(3))  # 7
