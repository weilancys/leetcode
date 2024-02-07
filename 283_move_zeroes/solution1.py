nums = [0, 1, 0, 3, 12]

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        left = 0
        right = size - 1

        while left < right:
            if nums[left] == 0:
                walk = left
                while walk < right:
                    nums[walk] = nums[walk+1]
                    walk += 1
                nums[right] = 0
                right -= 1
            else:
                left += 1

if __name__ == "__main__":
    solution1 = Solution()
    solution1.moveZeroes(nums)
    print(nums)