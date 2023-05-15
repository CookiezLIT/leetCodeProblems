import queue

class Solution:



    def lengthOfLongestSubstring(self, s: str) -> int:
        max_size = 0
        q = []
        for i in s:
            if not i in q:
                q.append(i)
                if len(q) > max_size:
                    max_size = len(q)
            else:
                while i in q:
                    q.pop(0)
                q.append(i)

        return max_size
    
s = Solution()
print(s.lengthOfLongestSubstring("abcdeabcde6"))