class RecentCounter:

    def __init__(self):
        # Items will be in asc order
        # Values on left would therefore start to become < t-3000
        # Hence popleft operation is needed. Pick deque
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        
        # Prune all items on left that are < t-3000
        while self.q[0] < self.q[-1] - 3000:
            self.q.popleft()
        
        return len(self.q)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
