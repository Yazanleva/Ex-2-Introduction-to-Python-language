# S3_LAM_02 — Sort by key (age ascending)

people = [
    {"name": "Ola", "age": 22},
    {"name": "Eva", "age": 19},
    {"name": "Adam", "age": 30},
]

print("before:", people)
sorted_people = sorted(people, key=lambda p: p["age"])
print("after:", sorted_people)
