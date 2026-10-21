class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x # Base cases: x = 0 or x = 1
        
        left, right = 1, x // 2
        
        while left <= right:
            mid = left + (right - left) // 2
            num_square = mid * mid
            
            if num_square == x:
                return mid
            elif num_square < x:
                left = mid + 1  
            else:
                right = mid - 1
        return right 
