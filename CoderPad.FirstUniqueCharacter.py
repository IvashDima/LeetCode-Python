# Задача 1 — First Unique Character
# Условие:
# Дана строка s. Верни индекс первого неповторяющегося символа. Если такого нет — верни -1.
#
# Пример:

# Input: "leetcode"
# Output: 0   // 'l' уникален и первый
#
# Input: "aabb"
# Output: -1

from collections import Counter

def firstUniqueCharacter(s: str) -> int:
    # result = -1
    # dublicated = ""
    counts = Counter(s)

    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
        # if ch in s[i+1:]:
        #     dublicated += letter
        #     continue
        # else:
        #     if ch in dublicated:
        #         continue
        #     else:
        #         result = i
        #         break
    return -1


print(firstUniqueCharacter("leetcode"))
