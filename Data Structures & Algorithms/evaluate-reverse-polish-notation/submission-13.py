class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        length = len(tokens)
        operands = deque()
        ans = int(tokens[0])
        for ch in tokens:
            match ch:
                case '+':
                    ans = operands.pop()
                    ans += operands.pop()
                case '-':
                    temp = operands.pop()
                    ans = operands.pop()-temp
                case '*':
                    ans = operands.pop()
                    ans *= operands.pop()
                case '/':
                    temp = operands.pop()
                    ans = int(operands.pop()/temp)
                case _:
                    operands.append(int(ch))
                    continue
            operands.append(ans)
        return ans