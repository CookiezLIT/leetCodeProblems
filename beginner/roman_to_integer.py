class Solution:
    """
    RULES:
    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
    """

    """
    VALUES:
    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    """

    def romanToInt(self, s: str) -> int:
        number = 0
        for count,value in enumerate(s):
            if value == 'M':
                number += 1000
            elif value == 'D':
                number += 500
            elif value == 'C':
                if count+1 < len(s) and (s[count+1] == 'D' or s[count+1] == 'M'):
                    number -= 100
                else:
                    number += 100
            elif value == 'L':
                number += 50
            elif value == 'X':
                if count+1 < len(s) and (s[count+1] == 'L' or s[count+1] == 'C'):
                    number -= 10
                else:
                    number += 10
            elif value == 'V':
                number += 5
            elif value == 'I':
                if count+1 < len(s) and (s[count+1] == 'V' or s[count+1] == 'X'):
                    number -= 1
                else:
                    number += 1 
        return number

c = Solution()

print(c.romanToInt("C"))
print(c.romanToInt("I"))
print(c.romanToInt("III"))
print(c.romanToInt("IV"))
print(c.romanToInt("IIII"))
print(c.romanToInt("MMXXIII"))
print(c.romanToInt("IM"))
