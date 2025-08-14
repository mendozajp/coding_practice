"""
https://neetcode.io/problems/anagram-groups?list=blind75
Very much reminds me of the previous question. Thinking we can pretty much do it the same. Set up
a dict with keys corresponding to the id of a list and values corresponding with the composition 
of the word letter by letter. Iterate through, if its there, return the key then append to the 
list at that index in the results, if not just append it to the list and add it to the dict with 
that index as its key. 
I feel this is sufficently fast enough. 
Also quick note, this neetcode.io site had some problems with class variables, so maybe avoid 
using them. Not that its doing it wrong, its just that it seems to init the solution class once
so if you're planning on using a class variable like we did eariler, then we would need to reset
it inbetween tests and we don't have access to that code, so keep it within function scope.
"""

class Solution:
    def init_or_add_to_anagrams(self, word: str, anagrams: dict) -> int:
        characters_org = {}
        if len(word) == 0:
            characters_org[""] = characters_org.get("", 0) + 1
        for character in word:
            characters_org[character] = characters_org.get(character, 0) + 1
        for key, value in anagrams.items():
            if characters_org == value:
                return key
        anagrams[len(anagrams)] = characters_org
        return len(anagrams) # return key for placement in results list, or add to end
    
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        result = []
        for word in strs:
            length = len(result)
            key = self.init_or_add_to_anagrams(word, anagrams)
            if key >= length:
                result.append([word])
            else:
                result[key].append(word)
        return result
    
"""
Conceptually okay, but also needlessly complicated.
The slower solution was just sorting and adding to list on comparisons. 
Though they did it in a cool way. 
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
    
"""
Not sure what default dict is but the key is the sorted list itself and the value is what we 
would return for the result which is pretty cool. I didn't think of that. 

The above is closer to what we did but probably a tiny bit worse since we don't sort, we
just iterate through. Guess its the same then since sorted() is O(n).

The other solution is basically the same but instead of sorting it iterates a list of 26 ints
corresponding to each char, then uses that entire list as the keys. Seemingly only slightly faster.
"""