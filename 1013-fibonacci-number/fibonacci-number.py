class Solution:
    def fib(self, n: int, dp={}) -> int:

        if n <= 1:
            dp[n] = n
            return n
        if n == 2:
            dp[2] = 1
            return 1

        left = dp[n-1] if n-1 in dp else self.fib(n-1)
        right = dp[n-2] if n-2 in dp else self.fib(n-2)

        return left + right
        