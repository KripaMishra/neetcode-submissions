import operator
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        stack = []
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                a = stack.pop(-1)
                b =stack.pop(-1)
                stack.append(int(operators[t](b, a)))
        return int(stack[-1])
