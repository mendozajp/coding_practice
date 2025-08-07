"""
https://leetcode.com/problems/simplify-path/description/
This might have been the easiest medium difficult question yet. Maybe its just easier on python. Parsing strings and manipuating them 
is not something I've done on many other languages.
Also didn't really end up doing anything interesting. The pattern I seem to follow is, can we get it into a list somehow because in 
python making changes of a list is incredibly easy. The past 2 questions were very much not that. That was the trap of them I guess
But this one I beat 100% of everyone by doing just that. 
Here it is.
"""

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        temp = path.split('/')
        result = []
        for segment in temp:
            if segment: 
                if segment == '.': continue
                if segment == "..": 
                    if len(result) > 0:
                        result.pop()
                        continue
                    else:
                        # limit going back
                        continue
                result.append(segment)
        if result:
            return "/" + "/".join(result)
        return "/"
    
"""
Really nothing crazy, just splitting by '/' which gets rid of all of them and isolates the file names, then just processing the 
indicated special cases and joining the result. 
Lets see what other people did. I hope it wasn't look at every single character. That would be insane. 

Yeah looks like the deciding factor was using a stack. Or I guess in python, just using pop to remove the last added item in the list.
This bit of code has some minor improvements to yours in terms of memory and kind of code cleanliness. 
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        for dir in path.split("/"):
            if dir == "" or dir == ".": continue
            if dir == "..":
                if stack: stack.pop()
            else:
                stack.append(dir)
        
        return "/" + "/".join(stack)
"""
So for this one we were pretty spot on. Shame for having that else continue instead of just a continue. Black linter is tossing in
its grave.
"""