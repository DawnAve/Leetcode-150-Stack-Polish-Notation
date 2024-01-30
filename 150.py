class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+','-','*','/']
        stack = []
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                second = stack.pop()
                first = stack.pop()
                if i == '+':
                    stack.append(second+first)
                elif i == '-':
                    stack.append(first-second)
                elif i == '*':
                    stack.append(first*second)
                elif i == '/':
                    stack.append(int(first/second))
        return stack[0]
