# 7. Подсчёт уникальных элементов
# Задача:
# Дан массив целых чисел. Верните количество элементов, которые встречаются только один раз.
#
# Пример:
# Input: nums = [1,2,2,3,4,4]
# Output: 2

from collections import Counter


def unicNumbers(nums: list[int]) -> int:
    count = 0
    counts = Counter(nums)

    for num in nums:
        if counts[num] == 1:
            count += 1
    return count # sum(1 for num in counts if counts[num] == 1)


print(unicNumbers([1,2,2,3,4,4]))