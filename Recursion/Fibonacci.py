print("hi")

# 1,1,2,3,5,7
def fibonacci(k):
  if k == 1 or k == 2:
    return 1
  elif k > 2:
    return fibonacci(k - 1) + fibonacci(k - 2)
  else:
    return "k must be positive"

for i in range(1):
  print(fibonacci(i))
