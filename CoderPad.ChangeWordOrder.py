# Задача 9 — Перевернуть слова в строке
# Условие:
# Дана строка s, содержащая слова, разделённые пробелами. Разверните порядок слов, сохранив порядок букв в словах.
# Пробелов в начале/конце быть не должно.
#
# Пример:
# Input: "  hello   world  "
# Output: "world hello"


def reverseWords(s: str) -> str:
    words = s.split()
    return " ".join(reversed(words))
    # rev_s = ""
    # for word in s.split():
    #     rev_s = word + " " + rev_s
    # return rev_s.strip()


print(reverseWords("  hello   world  "))