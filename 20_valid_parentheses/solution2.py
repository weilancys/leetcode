s1 = "({[]})"
s2 = "()[]{}"
s3 = "()[[]]"
s4 = "([)}"

# based on solution 1
# if one of ] } ) has to be put onto the stack, just return False immediately
# because in that case there's no chance it's a valid input

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
                        return False
                except IndexError:
                    return False
            elif letter == "}":
                try:
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
                except IndexError:
                    return False
            elif letter == "]":
                try:
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                except IndexError:
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    solution1 = Solution()
    result = solution1.isValid(s4)
    print(result)