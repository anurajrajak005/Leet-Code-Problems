class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest = 0
        s = set(nums)

        for x in s:
            if x - 1 not in s:
                i = 1
                while x + 1 in s:
                    x += 1     
                    i += 1
                longest = max(i, longest)
                
        return longest

    