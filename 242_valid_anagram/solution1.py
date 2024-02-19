# time complexity: O(n)
# space complexity: O(n)

# use a hashmap to keep track of all occurrences of each letter from each string
# if two strings are anagrams, their hashmaps should be exactly the same

s = "anagram"
t = "nagaram"

# s = "rat"
# t = "car"

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d_s = {}
        d_t = {}
        for c in s:
            d_s[c] = d_s.get(c, 0) + 1
        for c in t:
            d_t[c] = d_t.get(c, 0) + 1
        for k in d_s:
            if d_s.get(k) != d_t.get(k):
                return False
        return True

if __name__ == "__main__":
    solution1 = Solution()
    result = solution1.isAnagram(s, t)    
    print("is anagram:", result)