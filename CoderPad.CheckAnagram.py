# Задача 1 — Проверка анаграммы
# Даны две строки s и t. Определи, являются ли они анаграммами,
# то есть содержат ли они одинаковые буквы в одинаковом количестве, но, возможно, в другом порядке.
# Считаем, что входные строки содержат только строчные латинские буквы.
#
# Пример:
# Input: s = "anagram", t = "nagaram"
# Output: true
#
# Input: s = "rat", t = "car"
# Output: false

from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    # t_list = []
    # for i in t:
    #     t_list.append(i)
    # for i in s:
    #     if i in t_list:
    #         t_list.remove(i)
    # if not t_list:
    #     return True
    # return False
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


print(isAnagram("rat", "car"))
