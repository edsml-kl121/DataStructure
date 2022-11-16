def longest_substring(s):
  store_alphabet = []
  current_counter = 0
  max_counter = 0
  i = 0
  j = 0

  while i < len(s):
    if s[i] in store_alphabet:
      # max_counter = max(max_counter, current_counter)
      current_counter = 0
      store_alphabet = []
      j += 1
      i = j
    current_counter += 1
    max_counter = max(max_counter, current_counter)
    store_alphabet.append(s[i])
    print(store_alphabet)
    i += 1
  return max_counter

print(longest_substring("wwwff"))
