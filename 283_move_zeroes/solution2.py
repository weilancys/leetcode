nums = [0, 1, 0, 3, 12]

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        left = 0
        while left < size - 1:
            if nums[left] == 0:
                right = left + 1
                while right < size:
                    if nums[right] != 0:
                        temp = nums[right]
                        nums[right] = nums[left]
                        nums[left] = temp
                        break
                    right += 1
            left += 1


if __name__ == "__main__":
    solution2 = Solution()
    solution2.moveZeroes(nums)
    print(nums)