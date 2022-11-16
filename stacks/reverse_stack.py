# def reverseStack(stack):
#     if len(stack) == 0:
#       return
#     ans = [0] * len(stack)

#     top = stack.pop()
#     reverseStack(stack)
#     stack.insert(0, top)
#     return stack

def reverseStack(stack):
    ans = [0] * len(stack)
    stackreverseHelper(stack, ans, 0)
    return ans

def stackreverseHelper(stack, ans, i):
    if len(stack) == 0:
      return
    top = stack.pop()
    stackreverseHelper(stack, ans, i + 1)
    ans[i] = top

stack = [1,2,3,4,5]
print(reverseStack(stack))