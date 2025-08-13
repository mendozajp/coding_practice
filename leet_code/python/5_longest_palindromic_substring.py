"""
https://leetcode.com/problems/longest-palindromic-substring/description/
I didn't end up timing this one, but my thinking was, if we can find were a character appears 
again (at least twice) we have the minium bar for a palindrome so my hope was to parse thorugh
the right side of a list looking for specific characters that I see from the start, if I find them,
check them for palindromes, else keep looking. 

there are some big strings, and using in isnt as efficeint as you think, pretty sure its n worse 
case. It did end up working, but it was overall pretty slow. Only beating 23%
Not surprised it did as bad as it did with a nested loop in there. Idea may have been decent 
but execution was poor. 
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:

        def confirm_palindrome(arr: []) -> bool:
            return True if arr == arr[::-1] else False

        left = s[0] # take the first element, we'll test the rest with this
        left_marker = 1
        longest_palindrome = s[0]
        while left_marker < len(s):
            if left not in s[left_marker:]:
                left = s[left_marker]
                left_marker += 1 
                continue
            temp_id = 0
            for id, val in enumerate(s[left_marker:][::-1]):
                if left == val:
                    temp_id = len(s)-id
                    if confirm_palindrome(s[left_marker-1:temp_id]):
                        if len(longest_palindrome) < len(s[left_marker-1:temp_id]):
                            longest_palindrome = s[left_marker-1:temp_id]
            left = s[left_marker]
            left_marker += 1 

                
        return longest_palindrome
    
"""
Apparently this is already a thing. Manacher's Algorithm - used to find all palindromic substrings
solution is pretty werid though, gotta insert a bunch of stuff into the list and then have an 
expanding search range in the center. Pretty weird, don't get it right away, we should look back
at this later. They add abunch of stuff to the list to avoid needing seperate logic for even and
odds, but I'm not sure how it helps. 
most people seem to have a O(n^2) approach. don't wanna just throw code in here though. Revist
later.

"""