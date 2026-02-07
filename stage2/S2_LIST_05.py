# S2_LIST_05 — Stats

def stats(nums):
    if len(nums) == 0:
        return None

    mn = nums[0]
    mx = nums[0]
    total = 0

    for n in nums:
        if n < mn:
            mn = n
        if n > mx:
            mx = n
        total += n

    return {
        "min": mn,
        "max": mx,
        "avg": total / len(nums),
        "sum": total
    }


# Tests (including negatives)
print(stats([1, 2, 3, 4]))        # min=1 max=4 avg=2.5 sum=10
print(stats([-5, 0, 10, -2]))     # min=-5 max=10 ...
print(stats([]))                  # None
