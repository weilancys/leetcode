# time complexity: O(nlogn)
# space complexity: O(1)

# sort the nums array first and the majority element must be the middle element

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort() # for simplicity use sort method from builtin python list, which uses the Timsort algorithm with O(nlogn) time complexity. any sorting algorithm will do here.
        mid = 0 + (len(nums)-1-0) // 2
        return nums[mid]