import collections

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ans = collections.OrderedDict()
        

    def get(self, key: int) -> int:
        if key in self.ans:
            self.ans.move_to_end(key)
            return self.ans[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.ans:
            self.ans.move_to_end(key)

        self.ans[key] = value

        if len(self.ans) > self.capacity:
            self.ans.popitem(False)
        
