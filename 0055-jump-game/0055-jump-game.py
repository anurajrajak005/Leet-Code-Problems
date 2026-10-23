class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        checked = [False for i in range(n)]
        def check(cur):
            if cur == n-1:
                return True
            max_jump = nums[cur]
            if max_jump == 0:
                return False
            if cur + max_jump >= n-1:
                return True
            for i in range(max_jump, 0, -1):
                if checked[cur+i]:
                    continue
                else:
                    if check(cur+i):
                        return True
                    else:
                        checked[cur+i] = True
            return False
        return check(0)

        