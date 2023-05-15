class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        self.ans = s[0]
        
        for idx in range(1, len(s)):
            # odd case
            start, end = self.helper(idx, idx, s)
            if (end - start + 1) > len(self.ans):
                self.ans = s[start : end + 1]
            
            # even case
            start, end = self.helper(idx - 1, idx, s)
            if (end - start + 1) > len(self.ans):
                self.ans = s[start : end + 1]
        
        return self.ans
    
    # recursive solution
#     def helper(self, left, right, s):
#         if left < 0:
#             return (0, right - 1)
        
#         if right >= len(s):
#             return (left + 1, len(s) - 1)
        
#         if s[left] != s[right]:
#             return (left + 1, right - 1)
        
#         else:
#             return self.helper(left - 1, right + 1, s)
        
    # iterative solution
    def helper(self, left, right, s):
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            left -= 1
            right += 1
        
        return left + 1, right - 1

"""
Time Complexity:
helper method moves in both direction to find palidrome
So, for each index we need to perform this check. Which means it will cost O(n^2) in worst case. Time complexity same for iterative and recursive solution


Space complexity:
using helper method iteratively will save memory space here
iterative solution O(1)
recursive solution O(n)
"""

s = Solution()
print(s.longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))