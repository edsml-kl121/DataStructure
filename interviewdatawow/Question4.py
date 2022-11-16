def solution(A, K):
   # write your code in Python 3.6
   remaining_range = len(A) - K
   min_skip = 0
   max_skip = K
   current_amplitude = float('inf')
   for i in range(0, len(A) - K + 1):
      current_max = -float('inf')
      current_min = float('inf')
      # print(min_skip, max_skip)
      first_counter = False
      for i in range(len(A)):
         if i not in range(min_skip, max_skip):
            # print(A[i])
            current_max = max(current_max, A[i])
            current_min = min(current_min, A[i])
            # print("maxmin: ", current_max, current_min, current_amplitude)
            if first_counter:
               current_amplitude = min(current_amplitude, current_max - current_min)
            first_counter = True
      min_skip += 1
      max_skip += 1
   return current_amplitude

A = [5,3,6,1,3]
K = 2
print(solution(A, K))
A = [8, 8, 4, 3]
K = 2
print(solution(A, K))
A = [3,5,1,3,9,8]
K = 4
print(solution(A, K))

# print(5 in range(0,5))