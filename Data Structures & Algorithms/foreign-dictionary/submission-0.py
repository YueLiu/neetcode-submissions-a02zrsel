class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

#      Create a graph node for every unique character in all words.
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj}
# For each adjacent pair (w1, w2):
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
# If w1 starts with w2 and len(w1) > len(w2), return "".
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
# Find the first index j where they differ and add edge w1[j] -> w2[j] (only once).
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
# Increase indegree[w2[j]] when you add a new edge.
                        indegree[w2[j]] += 1
                    break
# Push all characters with indegree = 0 into a queue.
        q = deque([c for c in indegree if indegree[c] == 0])
        res = []
# While the queue is not empty:
        while q:
            char = q.popleft()
# Pop a character, add it to the answer.
            res.append(char)
            for neighbor in adj[char]:
# For each neighbor, decrement its indegree.
                indegree[neighbor] -= 1
# If a neighbor becomes 0, push it into the queue.
                if indegree[neighbor] == 0:
                    q.append(neighbor)
# If the answer contains fewer characters than total unique characters, a cycle exists - return "".
        if len(res) != len(indegree):
            return ""
# Otherwise, join the answer list and return it.
        return "".join(res)







