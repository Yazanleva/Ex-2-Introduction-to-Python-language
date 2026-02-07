# S1_IF_01 — Shipping cost

def shipping_cost(weight_kg, is_member):
    # validate
    if not isinstance(weight_kg, (int, float)) or weight_kg <= 0:
        return None

    if weight_kg <= 1:
        cost = 10
    elif weight_kg <= 5:
        cost = 20
    else:
        cost = 30

    if is_member:
        cost *= 0.8  # 20% discount

    return cost


# Tests (>=6 including boundaries)
tests = [
    (-1, False),
    (0, False),
    (0.5, False),
    (1, False),
    (5, False),
    (6, False),
    (3, True),
]

for w, m in tests:
    print(w, m, "->", shipping_cost(w, m))
