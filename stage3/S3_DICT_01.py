# S3_DICT_01 — Safe get by dotted path

def get_path(obj, path, fallback=None):
    if not isinstance(obj, dict):
        return fallback

    cur = obj
    for key in str(path).split("."):
        if not isinstance(cur, dict):
            return fallback
        if key not in cur:
            return fallback
        cur = cur[key]
    return cur


# Tests
data = {"a": {"b": {"c": 10}}, "x": None}
print(get_path(data, "a.b.c", "NO"))     # 10
print(get_path(data, "a.b.missing", "NO"))  # NO
print(get_path(data, "x.y", "NO"))       # NO
