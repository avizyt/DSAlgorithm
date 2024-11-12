import heapq


class PriorityQueue:
    def __init__(self) -> None:
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def is_empty(self):
        return len(self._queue) == 0

    def peek(self):
        return self._queue[0][-1] if not self.is_empty() else None

    def __len__(self):
        return len(self._queue)


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.push("task_low", priority=1)
    pq.push("task_medium", priority=5)
    pq.push("task_high", priority=4)

    # Pop items based on priority
    print("Items in priority order:")
    while not pq.is_empty():
        print(pq.pop())
