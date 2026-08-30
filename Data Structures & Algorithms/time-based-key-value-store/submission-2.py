class TimeMap:

    def __init__(self):
        from collections import defaultdict
        self.table=defaultdict(list) 
        # key : list of [value, timestamp] pairs



    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        key_values=self.table.get(key,[])
        # values array will be empty array if there are none.
        left=0
        right=len(key_values)-1
        result=""
        while left<=right:
            mid=(right+left)//2
            if key_values[mid][1]==timestamp:
                return key_values[mid][0]
            elif key_values[mid][1]<=timestamp:
                result=key_values[mid][0]
                left=mid+1
            else:
                right=mid-1
        return result