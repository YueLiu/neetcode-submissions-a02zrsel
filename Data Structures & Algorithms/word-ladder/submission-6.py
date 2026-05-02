class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # meet in the middle
        if endWord not in wordList or beginWord == endWord:
            return 0
        w = len(wordList[0])
        wordSet = set(wordList)
        visit1 = {beginWord: 1}
        visit2 = {endWord: 1}
        q1, q2 = deque([beginWord]), deque([endWord])

        while q1 and q2:
            if len(q1) > len(q2):
                q1, q2 = q2, q1
                visit1, visit2 = visit2, visit1
            for i in range(len(q1)):
                curr = q1.popleft()
                steps = visit1[curr]
                for j in range(w):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == curr[j]:
                            continue
                        nei = curr[:j] + c + curr[j+1:]
                        if nei not in wordSet:
                            continue
                        if nei in visit2:
                            return steps + visit2[nei]
                        if nei not in visit1:
                            visit1[nei] = steps + 1
                            q1.append(nei)
        return 0



