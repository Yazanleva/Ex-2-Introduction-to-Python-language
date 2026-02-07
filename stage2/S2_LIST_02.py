# S2_LIST_02 — Deduplicate without set (preserve first occurrence order)

def unique(values):
    out = []
    for v in values:
        if v not in out:
            out.append(v)
    return out


# Tests
print(unique([1, 2, 1, 3, 2, 4]))        # [1, 2, 3, 4]
print(unique(["a", "b", "a", "a", "c"])) # ['a', 'b', 'c']
