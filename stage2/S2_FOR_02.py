# S2_FOR_02 — Find first even (loop, no next())

def find_first_even(nums):
    for n in nums:
        if n % 2 == 0:
            return n
    return None


# Tests
print(find_first_even([1, 3, 5]))      # None
print(find_first_even([1, 3, 6, 8]))   # 6
print(find_first_even([2, 4, 6]))      # 2
