class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 그리디(X) --> 동적계획법으로
        
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if(i - coin >= 0):
                    dp[i] = min(dp[i], dp[i-coin]+1)

        if dp[amount] >= float('inf'):
            return -1

        return dp[amount]

        
# coins=[1,2,5] | amount=11

# i=1 -> dp=[0, 1, ...]
# i=2 -> dp=[0, 1, 1, ...], dp[2] vs dp[1]+1 // dp[2] vs dp[0]+1
# i=3 -> dp=[0, 1, 1, 2, ...], dp[3] vs dp[2]+1 // dp[3] vs dp[1]+1
# i=4 -> dp=[0, 1, 1, 2, 2, ...], dp[4] vs dp[3]+1 // dp[4] vs dp[2]+1
# i=5 -> dp=[0, 1, 1, 2, 2, 1, ...], dp[5] vs dp[4]+1 // dp[5] vs dp[3]+1 // dp[5] vs dp[0]+1
# i=6 -> dp=[0, 1, 1, 2, 2, 1, 2, ...], dp[6] vs dp[5]+1 // dp[6] vs dp[4]+1 // dp[6] vs dp[1]+1
# i=7 -> dp=[0, 1, 1, 2, 2, 1, 2, 2, ...], dp[7] vs dp[6]+1 // dp[7] vs dp[5]+1 // dp[7] vs dp[2]+1
# i=8 -> dp=[0, 1, 1, 2, 2, 1, 2, 2, 3, ...], dp[8] vs dp[7]+1 // dp[8] vs dp[6]+1 // dp[8] vs dp[3]+1
# i=9 -> dp=[0, 1, 1, 2, 2, 1, 2, 2, 3, 3, ...], dp[9] vs dp[8]+1 // dp[9] vs dp[7]+1 // dp[9] vs dp[4]+1
# i=10 -> dp=[0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, ...], dp[10] vs dp[9]+1 // dp[10] vs dp[8]+1 // dp[10] vs dp[5]+1
# i=11 -> dp=[0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3, ...], dp[11] vs dp[10]+1 // dp[11] vs dp[9]+1 // dp[11] vs dp[6]+1