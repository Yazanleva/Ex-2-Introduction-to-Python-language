# S2_FOR_06 — Sum nested lists (matrix)

def sum_nested(matrix):
    if not isinstance(matrix, list):
        return None

    total = 0
    for row in matrix:
        if not isinstance(row, list):
            return None
        for n in row:
            total += n
    return total


# Tests
print(sum_nested([[1, 2], [3, 4]]))     # 10
print(sum_nested([[10], [20, 30], []])) # 60
print(sum_nested([1, 2, 3]))            # None (invalid rows)
