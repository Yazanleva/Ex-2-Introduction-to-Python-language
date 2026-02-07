# S2_FOR_05 — Multiplication table 10x10 (1..10)

for r in range(1, 11):
    line = ""
    for c in range(1, 11):
        line += f"{r*c:4d}"
    print(line)
