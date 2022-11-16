def sortStack(stack):
  if len(stack) == 0:
    return
  
  top = stack.pop()
  sortStack(stack)
  insertStack(stack, top)
  return stack

def insertStack(stack, val):
  if len(stack) == 0 or val > stack[-1]:
    stack.append(val)
    return
  
  top = stack.pop()
  insertStack(stack, val)
  stack.append(top)

stack = [5,4,3,2,1]
print(sortStack(stack))