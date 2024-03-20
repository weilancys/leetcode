# time complexity: O(logn)
# space complexity: O(1)

# very similar to solution 1 but more fine grained control over the movement of the start and end pointers 
# and only call isBadVersion once each iteration
# more efficient than solution 1

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# this function is offered by leetcode without revealing the implementation
def isBadVersion(version: int):
    return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        while start < end:
            mid = start + (end-start) // 2
            cur = isBadVersion(mid)
            if cur:
                end = mid # not mid - 1 because cur could still be the version we're finding
            else:
                start = mid + 1 # mid + 1 because if cur is False, it can never be evaluated again
        return end