# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
#
# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"
#
# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
#
# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"
#
# Constraints:
# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.

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