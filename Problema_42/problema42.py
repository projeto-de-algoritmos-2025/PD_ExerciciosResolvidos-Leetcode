class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        memo = {}

        def dp(i):
            if i >= n - 1:
                return 0  

            if i in memo:
                return memo[i]

            min_jumps = float('inf')
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    min_jumps = min(min_jumps, 1 + dp(i + j))

            memo[i] = min_jumps
            return min_jumps

        return dp(0)
