class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord):
            return 0

        n = len(wordList)
        w = len(wordList[0])
        adj = [[] for _ in range(n)]
        wordMap = {}

        for i in range(n):
            wordMap[wordList[i]] = i

        for i in range(n):
            for j in range(i+1,n):
                count = 0
                for c in range(w):
                    if wordList[i][c] != wordList[j][c]:
                        count += 1
                if count == 1:
                    adj[i].append(j)
                    adj[j].append(i)
        q = deque()
        visit = set()
        for i in range(w):
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c == beginWord[i]:
                    continue
                word = beginWord[:i] + c + beginWord[i+1:]
                if word in wordMap and wordMap[word] not in visit:
                    q.append(wordMap[word])
                    visit.add(wordMap[word])
        ans = 1
        while q:
            ans += 1
            for i in range(len(q)):
                curr = q.popleft()
                if curr == wordMap[endWord]:
                    return ans
                for nei in adj[curr]:
                    if nei not in visit:
                        q.append(nei)
                        visit.add(nei)
        return 0

            

