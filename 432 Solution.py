class AllOne:

    def __init__(self):
        self.versions = defaultdict(int)
        self.minHeap = []
        self.maxHeap = []

    def inc(self, key: str) -> None:
        v = self.versions[key] + 1 
        heapq.heappush(self.minHeap, [v, key])
        heapq.heappush(self.maxHeap, [-v, key])
        self.versions[key] = v

    def dec(self, key: str) -> None:
        v = self.versions[key] - 1
        heapq.heappush(self.minHeap, [v, key])
        heapq.heappush(self.maxHeap, [-v, key])
        self.versions[key] = v

    def getMaxKey(self) -> str:
        while self.maxHeap:
            v = -1 * self.maxHeap[0][0]
            k = self.maxHeap[0][1]
            if self.versions[k] == v and v != 0:
                break
            heappop(self.maxHeap)
        if not self.maxHeap:
            return ""
        return self.maxHeap[0][1]

    def getMinKey(self) -> str:
        while self.minHeap:
            v = self.minHeap[0][0]
            k = self.minHeap[0][1]
            if self.versions[k] == v and v != 0:
                break
            heappop(self.minHeap)
        if not self.minHeap:
            return ""
        return self.minHeap[0][1]
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
