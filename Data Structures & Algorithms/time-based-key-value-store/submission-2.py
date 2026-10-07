class TimeMap:

    def __init__(self):
        self.d = defaultdict(str)
        self.strDict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[(key, timestamp)] = value
        self.strDict[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.strDict:
            return ""
        
        l = 0
        r = len(self.strDict[key])-1

        while l <= r:
            m = (l+r)//2
            if self.strDict[key][m] == timestamp:
                return self.d[(key, timestamp)]
            elif self.strDict[key][m] < timestamp:
                l = m+1
            else:
                r = m-1

        if r<0:
            return ""

            
        return self.d[(key, self.strDict[key][r])]