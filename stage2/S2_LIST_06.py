# S2_LIST_06 — Transform records

def active_user_names(users):
    names = [u["name"].upper() for u in users if u.get("active")]
    return sorted(names)


# Tests
users = [
    {"id": 1, "name": "ola", "active": True},
    {"id": 2, "name": "adam", "active": False},
    {"id": 3, "name": "eva", "active": True},
]
print(active_user_names(users))  # ['EVA', 'OLA']
