class Solution:
    def myPow(self, x: float, n: int) -> float:
        # brute-force solution of O(n)
        # if n > 0:
        #     pos_pow = x
        #     for _ in range(2, n + 1):
        #         pos_pow *= x
        #     return pos_pow
        # elif n < 0:
        #     neg_pow = x
        #     for _ in range(0, n - 1, -1):
        #         neg_pow /= x
        #     return neg_pow
        # return x if n else 1
        
        # optimal solution with fast power iteration
        # with O(logn) time and O(1) for space complexity
        N = n
        if n < 0:
            N = -N
            x = 1 / x
        
        ans = 1.0
        current_product = x
        while N > 0:
            if N % 2:
                ans *= current_product
            current_product *= current_product
            N //= 2    
        
        return ans
        
        # Python exclusive solution to never use
        # return x**n