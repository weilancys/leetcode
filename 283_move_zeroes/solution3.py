nums = [0, 1, 0, 3, 12]

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1


if __name__ == "__main__":
    solution3 = Solution()
    solution3.moveZeroes(nums)
    print(nums)