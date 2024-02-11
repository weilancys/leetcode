s1 = "({[]})"
s2 = "()[]{}"
s3 = "()[[]]"
s4 = "([)}"

# the main idea is to use a stack and put each parenthesis on the stack
# if the current parenthesis closes the previous one, pop the stack, otherwise put the current parenthesis on the stack
# fully closed parentheses should have a clean stack in the end

# time complexity: O(n)
# space complexity: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for letter in s:
            if letter == "(" or letter == "{" or letter == "[":
                stack.append(letter)
            elif letter == ")":
                try:
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        stack.append(letter)
                except IndexError:
                    return False
            elif letter == "}":
                try:
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        stack.append(letter)
                except IndexError:
                    return False
            elif letter == "]":
                try:
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        stack.append(letter)
                except IndexError:
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    solution1 = Solution()
    result = solution1.isValid(s2)
    print(result)