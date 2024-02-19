# time complexity: O(nlogn) since version 2.3 python list sort method uses timsort algorithm, which has the time complexity of O(nlogn)
# space complexity: O(n)

# sort each string and compare the sorted string
# if the sorted string are the same, return true, otherwise false
# less efficient than solution 1

# s = "anagram"
# t = "nagaram"

s = "rat"
t = "car"

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_sorted = self.sort(s)
        t_sorted = self.sort(t)
        return t_sorted == s_sorted
        
    def sort(self, s: str):
        l = [c for c in s]
        l.sort() # for simplicity, use default sort method of python list
        return "".join(l)


if __name__ == "__main__":
    solution2 = Solution()
    result = solution2.isAnagram(s, t)    
    print("is anagram:", result)