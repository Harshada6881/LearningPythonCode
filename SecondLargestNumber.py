# Find the Second Largest Number in a List

def second_largest(nums):
    unique_nums = list(set(nums))
    unique_nums.sort()
    return unique_nums[-2] if len(unique_nums) >= 2 else None
print(second_largest([4, 1, 3, 2, 5, 5]))  # Output: 4