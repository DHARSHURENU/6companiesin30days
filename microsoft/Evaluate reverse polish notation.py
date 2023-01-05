class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for t in tokens:
            if t not in {"+","-","*","/"}:
                stack.append(int(t))
            else:
                right,left = stack.pop(),stack.pop()
                if t == '+':
                     stack.append(left+right)
                elif t =='-':
                    stack.append(left-right)
                elif t =='*':
                    stack.append(left*right)
                elif t =='/':
                    stack.append(trunc(left/right))
        return stack[0]
