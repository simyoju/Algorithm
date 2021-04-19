import heapq

class PriorityQueue:
    def __init__(self):
        self.pq = []
        # self.pq.append(None)

    def is_empty(self):
        if len(self.pq) < 1:
            return True
        else:
            return False

    def put(self, data):
        heapq.heappush(self.pq, data)

    def get(self):
        if len(self.pq) < 1:
            return None
        return heapq.heappop(self.pq)

    def peek(self):
        print(self.pq)


pq = PriorityQueue()
pq.put((0, 'a'))
pq.put((5, 'b'))
pq.put((2, 'c'))
pq.put((1, 'd'))
pq.put((3, 'e'))
pq.put((4, 'f'))

pq.peek()
print(pq.is_empty())

print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.is_empty())