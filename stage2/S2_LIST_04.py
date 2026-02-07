# S2_LIST_04 — Flatten one level (manual, not recursive)

def flatten1(lst):
    out = []
    for item in lst:
        if isinstance(item, list):
            for x in item:
                out.append(x)
        else:
            out.append(item)
    return out


# Tests
print(flatten1([1, [2, 3], [4], 5]))     # [1,2,3,4,5]
print(flatten1([[1, 2], 3, [], [4]]))    # [1,2,3,4]
