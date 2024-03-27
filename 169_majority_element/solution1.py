# time complexity: O(n)
# space complexity: O(n)

# utilizing a hashmap to store all numbers and their occurrences
# traverse the hashmap and simply return the key with value larger than half length of the numbers array

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        lookup = {}
        for num in nums:
            lookup[num] = lookup.get(num, 0) + 1
        for k in lookup:
            if lookup[k] > len(nums) / 2:
                return k