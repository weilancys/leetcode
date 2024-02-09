nums = [2,7,11,15]
target = 9

# time complexity: O(n)
# space complexity: O(n)

# hashmap lookup is O(1) time complexity on average cases, O(n) on worst case which is rare
# this approach utilizes this fact and used a hashmap (dict in python) to speed up the search
class Solution:
    def twoSum(self, nums, target: int):
        registry = {}
        for i in range(len(nums)):
            registry[nums[i]] = i
        for j in range(len(nums)):
            complement = target - nums[j]
            if registry.get(complement) is not None and registry.get(complement) != j:
                return [j, registry.get(complement)]
        

if __name__ == "__main__":
    solution2 = Solution()
    result = solution2.twoSum(nums, target)
    print(result)