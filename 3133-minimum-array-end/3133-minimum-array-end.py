class Solution:
    def minEnd(self, n: int, x: int) -> int:
        remaining = n - 1
        result = x
        position = 1
        
        while remaining > 0:
            if (x & position) == 0:
                result |= (remaining & 1) * position
                remaining >>= 1
            position <<= 1
            
        return result
