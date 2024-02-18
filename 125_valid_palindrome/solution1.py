# time complexity: O(n)
# space complexity: O(n)

# first get rid of all non-alphanumeric chars in the string and make a new cleaned string
# then use two pointers pointing at both ends and progressivly compares the chars they point to before moving them towards each other
# just before the two pointers pass each other, stop

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
    solution1 = Solution()
    result = solution1.isPalindrome(s)
    print("is palindrome:", result)