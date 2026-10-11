class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        a , b = 0, len(nums)-1
        
        while a <= b :
            mid  = a+(b-a)//2
            if target == nums[mid] : 
                return mid 
            elif target < nums[mid] :
                b = mid -1
            else :
                a = mid+1
        return a               

  

