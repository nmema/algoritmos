'''
https://leetcode.com/problems/valid-parentheses/
time complexity -> O(n * log(n))
'''
class Solution:
    def isValid(self, s: str) -> bool:
        
        sides = {'(': ')',
                 '{': '}',
                 '[': ']'}
        
        if len(s) % 2 != 0 or s[0] not in sides:
            return False

        lifo = []
        
        for char in s:
            if char in sides:
                lifo.append(char)
            elif len(lifo) == 0 or char != sides.get(lifo[-1]):
                return False
            else:
                lifo.pop()

        return len(lifo) == 0