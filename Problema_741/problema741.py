class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)

        memo = {} 

        def dp(r1, c1, r2):
            c2 = r1 + c1 - r2

            if (r1 >= N or c1 >= N or r2 >= N or c2 >= N or
                grid[r1][c1] == -1 or grid[r2][c2] == -1):
                return float('-inf')

            if r1 == N - 1 and c1 == N - 1:
                return grid[r1][c1]

            if (r1, c1, r2) in memo:
                return memo[(r1, c1, r2)]

            current_cherries = grid[r1][c1]

            if (r1 != r2 or c1 != c2): 
                current_cherries += grid[r2][c2]

            max_prev_cherries = float('-inf')

            max_prev_cherries = max(max_prev_cherries, dp(r1 + 1, c1, r2 + 1))

            max_prev_cherries = max(max_prev_cherries, dp(r1 + 1, c1, r2))
     
            max_prev_cherries = max(max_prev_cherries, dp(r1, c1 + 1, r2 + 1))

            max_prev_cherries = max(max_prev_cherries, dp(r1, c1 + 1, r2))

            result = current_cherries + max_prev_cherries
            memo[(r1, c1, r2)] = result
            return result

        final_cherries = dp(0, 0, 0)

        return max(0, final_cherries)