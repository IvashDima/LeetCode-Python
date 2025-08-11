# Задача 11 — Проверить, можно ли составить строку
# Условие:
# Даны две строки ransomNote и magazine.
# Нужно определить, можно ли из букв magazine составить ransomNote.
# Каждую букву можно использовать только один раз.
#
# Пример:
# Input: ransomNote = "a", magazine = "b"
# Output: False
#
# Input: ransomNote = "aa", magazine = "aab"
# Output: True
from collections import Counter


def checkCreatingString(ransomNote: str, magazine: str) -> bool:
    # return ransomNote in magazine
    ransom_count = Counter(ransomNote)
    magazine_count = Counter(magazine)
    for char, count in ransom_count.items():
        if magazine_count[char] < count:
            return False
    return True


print(checkCreatingString("aa", "aab"))