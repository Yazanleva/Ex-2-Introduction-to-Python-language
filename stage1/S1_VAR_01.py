values = {
    "int": 1,
    "float": 1.5,
    "str": "hi",
    "bool": True,
    "none": None,
    "list": [1, 2],
    "tuple": (1, 2),
    "dict": {"a": 1},
    "set": {1, 2},
    "function": lambda x: x
}

for name, val in values.items():
    print(name, val, type(val), type(val).__name__)
