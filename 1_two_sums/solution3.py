nums = [2,7,11,15]
target = 9

# time complexity: O(n)
# space complexity: O(n)

# the third approach is based on the second, utilizing the fact that there's always a match in the array
# you add elements to the hashmap after you check complements, even though early added elements may search in an incomplete hashmap and not find a match
# later added elements will be sure to find its early added match
class Solution:
    def twoSum(self, nums, target: int):
        registry = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if registry.get(complement) is not None and registry.get(complement) != i:
                return [i, registry.get(complement)]
            registry[nums[i]] = i
        

if __name__ == "__main__":
    solution3 = Solution()
    result = solution3.twoSum(nums, target)
    print(result)