class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
            def dfs(j, cur):
                if j == len(word):
                    return cur.word
                
                c = word[j]
                if c == ".":
                    # 岔路口：尝试所有的门
                    for child in cur.children.values():
                        if dfs(j + 1, child):
                            return True
                    return False
                else:
                    # 单行道：只尝试一扇门
                    if c in cur.children:
                        return dfs(j + 1, cur.children[c]) # <--- 看这里！用递归代替了 for 循环里的 cur = ...
                    return False
                    
            return dfs(0, self.root)
        
        