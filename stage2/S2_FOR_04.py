# S2_FOR_04 — Count occurrences (histogram)

def count_occurrences(values):
    counts = {}
    for v in values:
        counts[v] = counts.get(v, 0) + 1
    return counts


# Tests
print(count_occurrences([1, 2, 1, 3, 2, 1]))  # {1: 3, 2: 2, 3: 1}
print(count_occurrences(["a", "b", "a"]))     # {'a': 2, 'b': 1}
