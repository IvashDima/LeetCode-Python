import re

class Solution:
    def reverseVowels(self, s: str) -> str:
        # exm_1
        # pattern = re.compile(r"[aeiou]", re.I)
        # vowels = pattern.findall(s)
        # v_index = len(vowels) - 1
        # result = []
        #
        # if 1 <= len(s) <= 300000 and s.isascii():
        #     for c in s:
        #         if pattern.match(c):
        #             result.append(vowels[v_index])
        #             v_index -= 1
        #         else:
        #             result.append(c)
        vowels = set("aeiouAEIOU")
        result = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and result[left] not in vowels:
                left += 1
            while left < right and result[right] not in vowels:
                right -= 1

            result[left], result[right]  = result[right], result[left]
            left += 1
            right -= 1

        return ''.join(result)

if __name__ == '__main__':
    solution = Solution()
    res = solution.reverseVowels("IceCreAm")
    print(res)