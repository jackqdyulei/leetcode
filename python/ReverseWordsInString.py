class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        items = reversed(s.split())
    	return " ".join(items)


# solution = Solution()
# print solution.reverseWords(" 1 2  3 4  ")