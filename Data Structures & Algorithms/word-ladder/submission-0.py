class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
        if endWord not in wordList:
            return 0
        adj = {}
        wordList.append(beginWord)
        for w in wordList:
            for i in range(len(w)):
                key = w[:i] + '*' + w[i+1:]
                adj[key] = adj.get(key, []) + [w]
        visited = set()
        q = [beginWord]
        visited.add(beginWord)
        step = 1
        while q:
            for _ in range(len(q)):
                w = q.pop(0)
                for i in range(len(w)):
                    key = w[:i] + '*' + w[i+1:]
                    for nei in adj[key]:
                        if nei == endWord:
                            return step+1
                        if nei in visited:
                            continue
                        visited.add(nei)
                        q.append(nei)
            step += 1
        return 0

