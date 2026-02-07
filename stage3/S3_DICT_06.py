# S3_DICT_06 — Group by property

def group_by(items, key):
    out = {}
    for item in items:
        group_key = item.get(key)
        if group_key not in out:
            out[group_key] = []
        out[group_key].append(item)
    return out


# Tests
people = [
    {"name": "Ola", "age": 20},
    {"name": "Eva", "age": 20},
    {"name": "Adam", "age": 30},
]
print(group_by(people, "age"))
