"""
https://neetcode.io/problems/is-palindrome?list=blind75
Pretty simple, but I had already known this one was best done with 2 pointers
and once you kinda know how 2 pointers work implementing it is pretty simple 
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = s
        temp = temp.lower()
        i, j = 0, len(temp)-1
        while i <= j:
            i_status = not temp[i].isalnum()
            j_status = not temp[j].isalnum()
            if i_status:
                i += 1
            if j_status:
                j -=1
            if i_status or j_status:
                continue
            if temp[i] == temp[j]:
                i += 1
                j -= 1
                continue
            return False
            
        return True