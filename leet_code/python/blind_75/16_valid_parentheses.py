"""
https://neetcode.io/problems/validate-parentheses?list=blind75
Stack questions are pretty easy since they're so fundamental. You know what a list is
and you pretty much know everything you need to know. Anything extra will just help you
do it faster. 
"""

class Solution:
    def isValid(self, s: str) -> bool:
        openers = []
        for i in s:
            if i in ['(','{','[']:
                openers.append(i)
                continue
            if i in [')', '}', ']']:
                if len(openers) == 0: return False
                last_open = openers.pop()
                if i == ')' and last_open == '(':
                    continue
                elif i == '}' and last_open == '{':
                    continue
                elif i == ']' and last_open == '[':
                    continue
                else:
                    return False
        if len(openers) > 0: return False
        return True
    

"""
All the ifs marginally slow it down im sure. The solution uses a dictionary for that closing
comparison which is pretty cool. Thats the only main difference. That and it handles the edge
cases slightly better.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:       # instead of poppoing right away they check and use the pop just to clear it. Does the same thing, but different order. This is cleaner
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False