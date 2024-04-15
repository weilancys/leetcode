# time complexity: O(n2) ?
# space complexity: O(1)

# brute force approach

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        largest_sum = min(nums)
        length = len(nums)
        for size in range(1, length+1):
            l = 0
            r = 0 + size - 1
            while r < length:
                sum = 0
                for i in range(l, r+1):
                    sum += nums[i]
                if sum > largest_sum:
                    largest_sum = sum
                l += 1
                r += 1
        return largest_sum



if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    solution = Solution()
    result = solution.maxSubArray(nums)
    print("result:", result)