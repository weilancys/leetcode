# time complexity: O(n)
# space complexity: O(n)

# iterate through the list and put each num in a hashmap
# if there's already a num in the hashmap, duplicate is found.

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        lookup = {}
        for num in nums:
            if num in lookup:
                return True
            else:
                lookup[num] = 0
        return False