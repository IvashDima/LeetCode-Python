class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return ' '.join(reversed(words))
        # result = []
        # word = ""
        #
        # for i in range(len(s)):
        #     if (s[i] == " "):
        #         if(word != ""): result.insert(0, word)
        #         word = ""
        #         continue
        #     else:
        #         word += s[i]
        # if(word != ""): result.insert(0, word)
        #
        # return ' '.join(result)

if __name__ == '__main__':
    solution = Solution()
    res = solution.reverseWords("  hello world  ")
    print("result:" + res + ".")