import bisect

class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        
        N = len(jobs)
        
        dp = [0] * (N + 1)
        
        for i in range(1, N + 1):
            current_start_time = jobs[i-1][0]
            current_end_time = jobs[i-1][1]
            current_profit = jobs[i-1][2]
            
            profit_without_current = dp[i-1]
            
            low, high = 0, i - 1
            prev_job_dp_idx = 0
            
            while low <= high:
                mid = (low + high) // 2
                if jobs[mid][1] <= current_start_time:
                    prev_job_dp_idx = mid + 1 
                    low = mid + 1 
                else:
                    high = mid - 1
            
            profit_with_current = current_profit + dp[prev_job_dp_idx]
                
            dp[i] = max(profit_without_current, profit_with_current)

        return dp[N]