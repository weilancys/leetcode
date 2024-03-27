# time complexity: O(n)
# space complexity: O(n)

# utilizing a hashmap to store all the occurrences of letters in s
# take pairs out of the hashmap and add to the length accordingly first
# then if any letter with more than zero occurrence is in the hashmap, add 1 to the length before returning it

class Solution:
    def longestPalindrome(self, s: str) -> int:
        lookup = {}
        length = 0
        has_one = False
        for l in s:
            lookup[l] = lookup.get(l, 0) + 1
        for k in lookup:
            length += lookup[k] // 2 * 2
            lookup[k] = lookup[k] % 2
            if lookup[k] > 0:
                has_one = True
        if has_one:
            length += 1
        return length
    
if __name__ == "__main__":
    s = "ccc"
    solution1 = Solution()
    result = solution1.longestPalindrome(s)
    print("result:", result)