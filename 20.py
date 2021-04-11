class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        right_brack = ['}', ']', ')']
        left_brack = ['{', '[', '(']
        for brack in s:
            if brack in right_brack:
                if len(stack) == 0:
                    return False
                l = stack.pop()
                if left_brack.index(l) != right_brack.index(brack):
                    return False
            else:
                stack.append(brack)
        return len(stack) == 0