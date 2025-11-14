class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0
        bank = set(bank)
        if endGene not in bank:
            return -1
        q = deque([startGene])
        visit = set()
        visit.add(startGene)
        res = 0
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endGene:
                    return res
                word = list(word)
                for i in range(8):
                    prev = word[i]
                    for c in ['A', 'C', 'T', 'G']:
                        word[i] = c
                        new_word = "".join(word)
                        if new_word in bank and new_word not in visit:
                            visit.add(new_word)
                            q.append(new_word)
                    word[i] = prev
            res += 1
        return -1
