# time complexity: O(n)
# space complexity: O(n)

# first use a hashmap to store letters and their occurrences
# then iterate through the ransom note and compare the letter with what's in the hashmap
# if the current letter is in the hashmap, reduce the occurrence accordingly or completely remove the letter from the hashmap
# otherwise just return false
# when the iteration is done, return true

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lookup = {}
        for letter in magazine:
            lookup[letter] = lookup.get(letter, 0) + 1
        for letter in ransomNote:
            if letter in lookup:
                if lookup[letter] > 1:
                    lookup[letter] = lookup[letter] - 1
                else:
                    lookup.pop(letter)
            else:
                return False
        return True