class Solution:

    """
    
    pentru fiecare caracter, vedem pe ce pozitii este
    si incercam sa ne dam seama matematic daca putem construi un palindrom

    ex:

    abba

    a: 0, 3
    b: 1, 2


    abcd123fff3
    
    a: 0
    b: 1
    c: 2
    d: 3
    1: 4
    2: 5
    3: 6,10
    f: 7,8,9



    """



    def palindrom(self, l):
        palindrom = True
        if len(l) == 1:
            return True
        for i in range(len(l)//2):
            if l[i] == l[len(l) - i -1]:
                pass
            else:
                palindrom = False
                break
        return palindrom


    def longestPalindrome(self, s: str) -> str:
        solution = [s[0]] if len(s) > 0 else []
        max = 1 # keeping the max of the longest list
        fast_stop = False
        for i in range(len(s)):
            deque = [s[i]] # initialize deque with current element 
            k = 1 # counter of elements that we can append to our substring
            cond_one = True # if we have elements to the left
            cond_two = True # if we have elements to the right

            while cond_one or cond_two:
                if i - k >= 0:
                    deque.insert(0,s[i-k]) # adaugam in stanga
                    if self.palindrom(deque) == True and len(deque) > max:
                        max = len(deque)
                        solution = str(deque)
                else:
                    cond_one = False
                if i + k < len(s): # adaugam in dreapta
                    deque.append(s[i+k])
                    if self.palindrom(deque) == True and len(deque) > max:
                        max = len(deque)
                        solution = str(deque)
                else:
                    cond_two = False
                if len(deque) == len(s) and self.palindrom(deque):
                    fast_stop = True
                    break
                k+=1
            if fast_stop == True:
                break
        f = ""
        for i in solution:
            if i.isalnum():
                f += i        
        return f

s = Solution()
# this exeeds the time limit:
#print(s.longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))



