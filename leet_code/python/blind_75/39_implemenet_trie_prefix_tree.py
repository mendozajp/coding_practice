"""
https://neetcode.io/problems/implement-prefix-tree?list=blind75
Trees really mess me up these days. Slowly getting a better grasp on it but Its a slow process
reading some articles and looked at the solution for this one. I had a lot of trouble when I
didnt have the TrieNode class, just its functionality in the PrefixTree init.
I basically could never figure out how to actually nest the objects linked list style
online people say its cause you need a root node thats empty to serve as the origin for all
searches and inserts, but I stil don't see why that cant just be the first set of children.
It gives you a list of every first letter available to you. I guess its cause if you dont assign
the PrefixTree to a specific object that you use the whole time and be extra careful about
attr management. Kinda thought I was but I guess not.

Regardless I was orginally doing that with arrs (wanted to do dicts for a while but chickened out)
and then looked at the solution. The dict solution is kinda what I was originally thinking, so I
just went about implementing that and got this.
"""


class TrieNode:

    def __init__(self):
        self.children = {}
        self.end_node = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        temp = self.root
        for c in word:
            if c not in temp.children.keys():
                temp.children[c] = TrieNode()
            temp = temp.children[c]
        temp.end_node = True

    def search(self, word: str, prefix: bool = False) -> bool:
        temp = self.root
        for c in word:
            if c not in temp.children:
                return False
            temp = temp.children[c]
        if temp.end_node or prefix:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, True)
