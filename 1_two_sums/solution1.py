nums = [2,7,11,15]
target = 9

# brute force approach
class Solution:
    def twoSum(self, nums, target: int):
        size = len(nums)
        left = 0
        while left < size - 1:
            right = left + 1
            while right < size:
                if nums[left] + nums[right] == target:
                    return [left, right]
                right += 1
            left += 1

if __name__ == "__main__":
    solution1 = Solution()
    result = solution1.twoSum(nums, target)
    print(result)