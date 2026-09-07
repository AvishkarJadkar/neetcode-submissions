class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in "+-*/":
                b, a = stack.pop(), stack.pop()

                if t == "+":
                    result = a + b
                elif t == "-":
                    result = a - b
                elif t == "*":
                    result = a * b

                else:
                    result = int(a/b)

                stack.append(result)

            else:
                stack.append(int(t))

        return stack[0]