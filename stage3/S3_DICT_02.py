# S3_DICT_02 — Merge defaults (shallow)

def merge_defaults(defaults, overrides):
    # Python 3.9+: {**defaults, **overrides} or defaults | overrides
    return {**defaults, **overrides}


# Tests (show shallow behavior)
defaults = {"host": "localhost", "opts": {"debug": False}}
overrides = {"port": 8080, "opts": {"debug": True}}

merged = merge_defaults(defaults, overrides)
print("merged:", merged)

# Shallow merge: nested dict is replaced, not merged deeply
print("defaults opts:", defaults["opts"])
print("merged opts:", merged["opts"])
