class TimeMap:

    def __init__(self):
        self.keyStore = {} # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            mid = l + (r-l)//2
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                ans = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return ans