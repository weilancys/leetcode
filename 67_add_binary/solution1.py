# time complexity: O(n)
# space complexity: O(n)

# pay attention to the carry bit, set it when it should
# all else is just binary arithmetic

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = False
        r_idx_a = len(a) - 1
        r_idx_b = len(b) - 1
        idx_a = r_idx_a
        idx_b = r_idx_b

        while idx_a >= 0 and idx_b >= 0:
            if a[idx_a] != b[idx_b]:
                if carry:
                    result = "0" + result
                    carry = True
                else:
                    result = "1" + result
            elif a[idx_a] == '0':
                if carry:
                    result = "1" + result
                    carry = False
                else:
                    result = "0" + result
            else:
                if carry:
                    result = "1" + result
                else:
                    result = "0" + result
                    carry = True
            idx_a -= 1
            idx_b -= 1

        while idx_a >= 0:
            if a[idx_a] == '0':
                if carry:
                    result = '1' + result
                    carry = False
                else:
                    result = '0' + result
            elif a[idx_a] == '1':
                if carry:
                    result = '0' + result
                    carry = True
                else:
                    result = '1' + result
            idx_a -= 1
        while idx_b >= 0:
            if b[idx_b] == '0':
                if carry:
                    result = '1' + result
                    carry = False
                else:
                    result = '0' + result
            elif b[idx_b] == '1':
                if carry:
                    result = '0' + result
                    carry = True
                else:
                    result = '1' + result
            idx_b -= 1
        
        if carry:
            result = "1" + result

        return result

if __name__ == "__main__":
    a = "101111"
    b = "10"
    solution = Solution()
    result = solution.addBinary(a, b) # expects "110001"
    print("result:", result)