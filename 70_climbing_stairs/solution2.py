# time complexity: O(n)
# space complexity: O(1)

# dynamic programming approach, very efficient

class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1
        for i in range(2, n+1):
            temp = one
            one = one + two
            two = temp
        return one

if __name__ == "__main__":
    solution = Solution()
    result = solution.climbStairs(38) # result should be 63245986 when n = 38
    print("result:", result)
    