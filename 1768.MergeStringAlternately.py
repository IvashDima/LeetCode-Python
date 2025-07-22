# You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.
#
# Example 1:
#
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_str: str = ''
        count: int
        if len(word1) > len(word2):
            count = len(word1)
        else:
            count = len(word2)

        if 1 <= count <= 100:
            for i in range(count):
                if i < len(word1):
                    merged_str += word1[i]
                if i < len(word2):
                    merged_str += word2[i]
        return merged_str

if __name__ == '__main__':
    solution = Solution()
    res = solution.mergeAlternately("abcd", "pq")
    print(res)
    list = []
    list.append()
