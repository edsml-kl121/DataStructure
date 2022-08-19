print("hi")

# Time complexity 2^n, o(n) space
    #   fib(6)
    #   /     \
    # fib(5)  fib(4)
#    /      \     /  \
# fib(4)  fib(3)

# time(Fib(n)) = time(Fib(n-1)) + time(Fib(n-2)) + .. + time(Fib(1))

def fibonacci(k):
  if k == 1 or k == 2:
    return 1
  elif k > 2:
    return fibonacci(k - 1) + fibonacci(k - 2)
  else:
    return "k must be positive"

def fibonacci_n(k):
  if k == 1 or k == 2:
    return 1
  elif k > 2:
    initial = [1, 1]
    for _ in range(k-2):
      next_num = initial[0] + initial[1]
      previous = initial[1]
      initial = [previous, next_num]
    return initial[-1]
  else:
    return "insert > 0"


for i in range(10):
  print(fibonacci_n(i))



