# S3_DICT_04 — Omit keys

def omit(d, keys):
    remove = set(keys)
    out = {}
    for k, v in d.items():
        if k not in remove:
            out[k] = v
    return out


# Tests
cfg = {"host": "localhost", "port": 3000, "secret": "123"}
print(omit(cfg, ["secret"]))  # {'host': 'localhost', 'port': 3000}
print(cfg)  # original unchanged
