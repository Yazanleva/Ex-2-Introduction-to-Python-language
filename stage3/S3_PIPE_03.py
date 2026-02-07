# S3_PIPE_03 — String normalization pipeline

import re

def pipe(*fns):
    def run(x):
        for fn in fns:
            x = fn(x)
        return x
    return run

strip_ = lambda s: s.strip()
lower_ = lambda s: s.lower()
collapse_spaces = lambda s: re.sub(r"\s+", " ", s)

normalize = pipe(strip_, lower_, collapse_spaces)

print(normalize(" Ala  Ma   Kota  "))  # "ala ma kota"
