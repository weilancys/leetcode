# time complexity: O(n)
# space complexity: O(1)

# most optimal approach for this question
# the main idea is that as you traverse the array, cross out elements that are different, eventually only the majority element will be left in the array

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        majority = None
        count = 0
        for num in nums:
            if not majority:
                majority = num
                count = 1
            elif majority == num:
                count += 1
            else:
                if count == 1:
                    majority = None
                    count = 0
                elif count > 1:
                    count -= 1
        return majority
    

if __name__ == "__main__":
    nums = [2,2,1,1,1,2,2]
    solution3 = Solution()
    majority = solution3.majorityElement(nums)
    print("majority:", majority)
