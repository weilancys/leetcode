# time complexity: O(n)
# space complexity: O(1)

# this approach is based on solution 1 but doesn't introduce a new string
# use two pointers and move them towards each other as the chars they point to are compared
# if a non-alphanumeric char is pointed at, just move along 

# s = "A man, a plan, a canal: Panama"
# s = "race a car"
# s = " "
s = ".,"

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        diff = ord('a') - ord('A')
        while l < r:
            code_l = ord(s[l])
            if (code_l < 48) or (code_l > 57 and code_l < 65) or (code_l > 90 and code_l < 97) or (code_l > 122):
                l += 1
                continue
            code_r = ord(s[r])
            if (code_r < 48) or (code_r > 57 and code_r < 65) or (code_r > 90 and code_r < 97) or (code_r > 122):
                r -= 1
                continue
            if code_l >= 65 and code_l <= 90:
                code_l += diff
            if code_r >= 65 and code_r <= 90:
                code_r += diff
            if chr(code_l) != chr(code_r):
                return False
            l += 1
            r -= 1
        return True

if __name__ == "__main__":
    solution2 = Solution()
    result = solution2.isPalindrome(s)
    print("is palindrome:", result)