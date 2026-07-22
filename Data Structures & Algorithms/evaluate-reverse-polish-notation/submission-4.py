import operator
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        stack = []
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
                print("Appended : ",int(t))
            else:
                a = stack.pop(-1)
                print("A is:",a)
                b =stack.pop(-1)
                print("B is:",b)
                stack.append(int(operators[t](b, a)))
                print("Appended : ",operators[t](b, a))
        return int(stack[-1])
