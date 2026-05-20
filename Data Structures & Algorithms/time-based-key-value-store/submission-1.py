class TimeMap:

    # each key stores its values in order they were inserted
    # timestamps are guaranteed to be increasing for each key
    # => Since timestamp is sorted, we can use binary search to find this position

    # lets keep a list of (value, timestamp) pairs for each key.

    def __init__(self):
        # dictionary: key / list of [value, timestamp]
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = [] # [value, timestamp]
        self.keyStore[key].append([value, timestamp])

    # applying binary search utilizing increasing timestamp trait
    def get(self, key: str, timestamp: int) -> str:
        res = "" # if no answer

        # getting the list for this key we are interested in
        values = self.keyStore.get(key, []) # -> list of [value, timestamp] for that key

        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2
            # if valid answer, first save it, but know that there could be something larger that still works
            if values[m][1] <= timestamp: # [m][1] = timestamp
                res = values[m][0] # [m][0] = value
                l = m + 1
            # if timestamp too large, look at smaller values.
            else:
                r = m - 1

        return res
            
