lst = [1, 2, 3]
lst[0] = 99
print(lst)

tpl = (1, 2, 3)
try:
    tpl[0] = 99
except Exception as e:
    print("Error:", e)

# Lists are mutable; tuples are immutable.
