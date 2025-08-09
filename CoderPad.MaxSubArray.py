# Задача 2 — Максимальная сумма подмассива (Kadane’s Algorithm)
# Условие:
# Дан массив целых чисел (положительных и отрицательных).
# Найди максимальную сумму непрерывного подмассива.
# Подмассив должен содержать хотя бы один элемент.
#
# Пример:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: Подмассив [4,-1,2,1] имеет максимальную сумму = 6
#
# Input: nums = [1]
# Output: 1
#
# Input: nums = [5,4,-1,7,8]
# Output: 23


def maxSubArray(nums: list[int]) -> int:
    count = len(nums)
    max_sum = sum(nums)
    i = 0
    j = count
    while i < j:
        while i < j and sum(nums[i:j]) > max_sum:
            max_sum = sum(nums[i:j])
            i += 1
        while i < j and sum(nums[i:j]) > max_sum:
            max_sum = sum(nums[i:j])
            j -= 1
        i += 1
        j -= 1
    return max_sum


print(maxSubArray([5,4,-1,7,8]))