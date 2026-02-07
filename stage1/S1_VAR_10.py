def inspect(v):
    try:
        iterable = True
        iter(v)
    except Exception:
        iterable = False

    return {
        "type_name": type(v).__name__,
        "is_none": v is None,
        "is_callable": callable(v),
        "is_iterable": iterable,
        "truthy": bool(v)
    }

tests = [0, 1, "", [], [1], {}, None, lambda x: x]

for t in tests:
    print(t, inspect(t))
