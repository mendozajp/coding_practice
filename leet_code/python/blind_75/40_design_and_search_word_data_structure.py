"""
https://neetcode.io/problems/design-word-search-data-structure?list=blind75
Yesterday we looked up how to go about implementing the Trie data structure with some functionality
after finally getting how it all worked - dang trees were really messing with me
I wanted to just try the next one.
Bit anooying getting started, but once we kinda had a thought going (mainly on how we'd go about . searches)
we really started cooking. Took longer then I would technically allow, but since we're still pretty new to
trees I'll forgive it. It'll come with time.
What happened to your doc string practice? bring those back
more comments too, you looking back in a year is gonna be confused.
"""


class TreeNode:
    def __init__(self):
        self.children = {}
        self.final_node = False


class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        if "." in word:
            print("assumption wrong, inserting word with .")
        node = self.root
        for idx, c in enumerate(word):
            if c in node.children:
                node = node.children[c]
            else:
                node.children[c] = TreeNode()
                if idx == len(word) - 1:
                    node.children[c].final_node = True
                node = node.children[c]
        return None

    def blanket_search(self, dot_node: TreeNode, subword: str) -> bool:
        if not subword:  # handle last char being '.' case
            # search all children for a node with final node, if there is true, else false
            for child in dot_node.children:
                if dot_node.children[child].final_node:
                    return True
            return False
        for child in dot_node.children:  # all nodes in the layer we can pick anything
            temp = dot_node.children[child]
            for idx, c in enumerate(subword):
                if c == ".":
                    if self.blanket_search(dot_node=temp, subword=subword[idx + 1 :]):
                        return True
                    break
                if c in temp.children:
                    temp = temp.children[c]
                    if idx == len(subword) - 1:
                        return True
        return False

    def search(self, word: str) -> bool:
        temp = self.root
        for idx, c in enumerate(word):
            if c == ".":
                return self.blanket_search(temp, word[idx + 1 :])
            if c in temp.children:
                temp = temp.children[c]
            else:
                return False
        return True
