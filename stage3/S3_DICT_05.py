# S3_DICT_05 — Invert with collisions

def invert(d):
    out = {}
    for k, v in d.items():
        if v not in out:
            out[v] = k
        else:
            # collision: store list of keys
            existing = out[v]
            if isinstance(existing, list):
                existing.append(k)
            else:
                out[v] = [existing, k]
    return out


# Tests
print(invert({"a": 1, "b": 2}))            # {1: 'a', 2: 'b'}
print(invert({"a": 1, "b": 1, "c": 2}))    # {1: ['a','b'], 2: 'c'}
