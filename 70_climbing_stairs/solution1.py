# time complexity: O(2 to the power of n)
# space complexity: O(1)

# brute force approach, not efficient at all
# make a decision tree out of all the decisions that can be made on each step
# traverse the tree in dfs manner
# when a path is found, add one to the path count

class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        count = self.walk(n, 0, 1, count)
        count = self.walk(n, 0, 2, count)
        return count

    def walk(self, n, cur, step, count):
        if cur + step < n:
            count = self.walk(n, cur+step, 1, count)
            count = self.walk(n, cur+step, 2, count)
        elif cur + step == n:
            count += 1
        return count


if __name__ == "__main__":
    solution = Solution()
    result = solution.climbStairs(38)
    print("result:", result)