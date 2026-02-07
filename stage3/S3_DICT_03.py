# S3_DICT_03 — Pick keys

def pick(d, keys):
    out = {}
    for k in keys:
        if k in d:
            out[k] = d[k]
    return out


# Tests
user = {"id": 1, "name": "Ola", "age": 20}
print(pick(user, ["id", "name", "missing"]))  # {'id': 1, 'name': 'Ola'}
