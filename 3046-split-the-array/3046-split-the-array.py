from collections import Counter

class Solution:
    def isPossibleToSplit(self, nums: list[int]) -> bool:
        counts = Counter(nums)
        
        for num, frequency in counts.items():
            if frequency > 2:
                return False
                
        return True
