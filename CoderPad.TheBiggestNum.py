# Задача 10 — Найти k-й по величине элемент
# Условие:
# Дан массив nums и число k. Найдите k-й по величине элемент массива (k начинается с 1).
#
# Пример:
#
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
import heapq


def theBiggestNum(nums: list[int], k: int) -> int:
    # return sorted(nums)[-k]
    return heapq.nlargest(k, nums)[-1]


print(theBiggestNum([3,2,1,5,6,4], 2))