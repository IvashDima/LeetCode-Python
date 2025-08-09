# Задача 1 — Проверка анаграммы
# Даны две строки s и t. Определи, являются ли они анаграммами (содержат одинаковые буквы в любом порядке).


def isAnagram(s: str, t: str) -> bool:
    for i in s:
        for j in t:
            if i == j:
                return True
    return False


print(isAnagram("LEET","CODE"))
