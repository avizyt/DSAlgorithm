def subsets(nums):
    if not nums:
        return [[]]
    x = subsets(nums[1:])
    return x + [[nums[0]] + y for y in x]

print(subsets([1,2,3,4,5]))