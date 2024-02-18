s = "A man, a plan, a canal: Panama"
# s = "race a car"
# s = " "

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cleaned = self.clean(s)
        l = 0
        r = len(s_cleaned) - 1
        while l < r:
            if s_cleaned[l] != s_cleaned[r]:
                return False
            l += 1
            r -= 1
        return True

    def clean(self, s) -> str:
        # 48 - 57  --  '0' - '9'
        # 65 - 90  --  'A' - 'Z'
        # 97 - 122 --  'a' - 'z'
        diff = ord("a") - ord("A")
        s_cleaned = ""
        for letter in s:
            code = ord(letter)
            if code >= 48 and code <= 57 or code >= 97 and code <= 122:
                s_cleaned += letter
            elif code >= 65 and code <= 90:
                s_cleaned += chr(ord(letter) + diff)
        return s_cleaned

if __name__ == "__main__":
    solution = Solution()
    result = solution.isPalindrome(s)
    print("is palindrome:", result)