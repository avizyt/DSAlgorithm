"""Question 3.44 (Algorithm Design Manual)
You have an unordered array X of n integers. Find the array M containing
n elements where Mi is the product of all integers in X except for Xi. You may
not use division. You can use extra memory
"""


def product_except_self(nums):
    n = len(nums)
    if n == 0:
        return []

    left = [1] * n
    right = [1] * n
    result = [1] * n

    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]

    for i in range(n):
        result[i] = left[i] * right[i]
    return result


def product_except_self2(nums):
    n = len(nums)
    if n == 0:
        return []

    result = [1] * n

    for i in range(1, n):
        result[i] = result[i - 1] * nums[i - 1]

    right_cumulative = 1
    for i in range(n - 1, -1, -1):
        result[i] = result[i] * right_cumulative
        right_cumulative *= nums[i]

    return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    output = product_except_self2(nums)
    print("Input:", nums)
    print("Output:", output)
