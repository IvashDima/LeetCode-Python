# Условие:
# Дана строка s. Верни индекс первого неповторяющегося символа. Если такого нет — верни -1.
#
# Пример:

# Input: "leetcode"
# Output: 0   // 'l' уникален и первый
#
# Input: "aabb"
# Output: -1

def firstUniqueCharacter(s: str):
    result = -1
    dublicated = ""

    for i, letter in enumerate(s):
        if letter in s[i+1:]:
            dublicated += letter
            continue
        else:
            if letter in dublicated:
                continue
            else:
                result = letter
                break
    return result

s = "leetcode"
print(firstUniqueCharacter(s))
