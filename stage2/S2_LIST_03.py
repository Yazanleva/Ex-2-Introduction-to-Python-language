# S2_LIST_03 — Chunk a list

def chunk(lst, size):
    if size <= 0:
        return None

    out = []
    i = 0
    while i < len(lst):
        out.append(lst[i:i+size])
        i += size
    return out


# Tests
print(chunk([1, 2, 3, 4, 5], 2))  # [[1,2],[3,4],[5]]
print(chunk([1, 2, 3], 0))        # None
