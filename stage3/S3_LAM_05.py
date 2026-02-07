# S3_LAM_05 — Higher-order predicate

def at_least(min_value):
    return lambda n: n >= min_value

nums = [1, 5, 10, 15]
print(list(filter(at_least(10), nums)))  # [10, 15]
