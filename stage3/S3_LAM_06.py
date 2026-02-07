# S3_LAM_06 — Map values in a dict

def map_values(d, fn):
    return {k: fn(v) for k, v in d.items()}

prices = {"apple": 2, "orange": 3}
doubled = map_values(prices, lambda v: v * 2)

print(doubled)  # {'apple': 4, 'orange': 6}
print(prices)   # original unchanged
