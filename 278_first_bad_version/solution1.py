# time complexity: O(logn)
# space complexity: O(1)

# try to search for the first bad version in a binary search manner
# search for the middle version and decide if it is bad or good
# if it's bad and its previous version is good, the search is done
# otherwise, if the version is good, continue the binary search to the right half
# if the version is bad, continue the binary search to the left half

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# this function is offered by leetcode without revealing the implementation
def isBadVersion(version: int):
    return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        while start <= end:
            mid = start + (end-start) // 2
            cur = isBadVersion(mid)
            if mid > 1:
                prev = isBadVersion(mid-1)
            else:
                prev = False
            if not prev and cur:
                return mid
            if cur:
                end = mid - 1
            else:
                start = mid + 1
        return n
