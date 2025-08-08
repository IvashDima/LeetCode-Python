# Задача 3 — Valid Parentheses
# Условие:
# Дана строка, содержащая символы '(', ')', '{', '}', '[', ']'.
# Верни true, если скобки расставлены корректно.
#
# Пример:
#
# vbnet
# Copy
# Edit
# Input: "()[]{}"
# Output: true
#
# Input: "(]"
# Output: false


def validParentheses(s: str):
    result = True
    for i, el in enumerate(s):
        if el == '(':
            if s[i+1] == ')':
                continue
            else:
                result = False
                break
        if el == '{':
            if s[i+1] == '}':
                continue
            else:
                result = False
                break
        if el == '[':
            if s[i+1] == ']':
                continue
            else:
                result = False
                break

    return result


print(validParentheses("()[]{}"))