# Задача 3 — Два числа в сумме дают target
# Условие:
# Дан массив целых чисел nums и число target. Нужно вернуть индексы двух чисел, сумма которых равна target.
# Можно считать, что существует ровно одно решение, и одно и то же число не используется дважды.
#
# Пример:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: nums[0] + nums[1] = 2 + 7 = 9
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Input: nums = [3,3], target = 6
# Output: [0,1]

from functools import reduce


def twoSum(nums: list[int], target: int) -> list[int]:
    result = []
    i = 0
    j = len(nums)-1
    while i < j:
        print(nums[i]+nums[j])
        while i < j:
            if nums[i]+nums[j] == target:
                result.append(nums[i])
                result.append(nums[j])
                return result
            else:
                i += 1
        i = 0
        while i < j:
            if nums[i]+nums[j] == target:
                result.append(nums[i])
                result.append(nums[j])
                return result
            else:
                j -= 1
        i += 1
        j -= 1

    return result


print(twoSum([3,3], 6))