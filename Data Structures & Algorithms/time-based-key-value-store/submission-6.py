class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        timeline = self.time_map[key]
        l, r = 0, len(timeline) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2
            t, v = timeline[mid]
            if t <= timestamp:
                res = v
                l = mid + 1
            else:
                r = mid - 1

        return res
