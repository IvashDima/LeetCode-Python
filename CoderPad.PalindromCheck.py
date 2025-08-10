# 8. Проверка палиндрома
# Задача:
# Дана строка s. Верните True, если она читается одинаково слева направо и справа налево (игнорируя регистр и неалфавитные символы).
#
# Пример:
# Input: "A man, a plan, a canal: Panama"
# Output: True
#
# Input: "race a car"
# Output: False

import re


def palindromCheck(s: str) -> bool:
    lower_s = re.sub('[^a-z]','', s.lower())
    i, j = 0 , len(lower_s)-1
    while i < j:
        if lower_s[i] == lower_s[j]:
            i += 1
            j -= 1
            continue
        else:
            return False

    return True


print(palindromCheck("race a car"))