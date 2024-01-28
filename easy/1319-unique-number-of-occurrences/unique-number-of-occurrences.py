class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = {}
        for num in arr:
            if num in occurences.keys():
                occurences[num] = occurences[num] + 1
            else:
                occurences[num] = 1
        values = list(occurences.values())
        values.sort()
        last = 0
        for val in values:
            if val == last:
                return False
            last = val
        return True
            