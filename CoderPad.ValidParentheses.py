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


def validParentheses(s: str) -> bool:
    # result = True
    # for i, el in enumerate(s):
    #     if el == '(':
    #         if s[i+1] == ')':
    #             continue
    #         else:
    #             result = False
    #             break
    #     if el == '{':
    #         if s[i+1] == '}':
    #             continue
    #         else:
    #             result = False
    #             break
    #     if el == '[':
    #         if s[i+1] == ']':
    #             continue
    #         else:
    #             result = False
    #             break
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for ch in s:
        if ch in mapping.values():
            stack.append(ch)
        elif ch in mapping:
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()

    return not stack


print(validParentheses("()[]{}"))