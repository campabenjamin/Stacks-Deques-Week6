class Deque:
    def __init__(self, capacity=5):
        self._data = []
        self._capacity = capacity

    def is_empty(self):
        return len(self._data) == 0

    def is_full(self):
        return len(self._data) >= self._capacity

    def add_back(self, item):
        if not self.is_full():
            self._data.append(item)

    def add_front(self, item):
        if not self.is_full():
            self._data.insert(0, item)

    def remove(self, item):
        if item in self._data:
            self._data.remove(item)
            return True
        return False

    def remove_back(self):
        if not self.is_empty():
            return self._data.pop()
        return None

    def __str__(self):
        return str(self._data)
    