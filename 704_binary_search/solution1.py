# time complexity: O(logn)
# space complexity: O(1)

# classic binary search algorithm
# https://en.wikipedia.org/wiki/Binary_search_algorithm

nums = [-1,0,3,5,9,12]
target = 9

# nums = [-1,0,3,5,9,12]
# target = 2

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        m = (l + r) // 2
        while l <= r:
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
            m = (l + r) // 2
        return -1

if __name__ == "__main__":
    solution1 = Solution()
    index = solution1.search(nums, target)
    print("index:", index)
    
