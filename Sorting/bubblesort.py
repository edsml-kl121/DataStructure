def bubbleSort(nums):
  loop = True
  while loop == True:
      loop = False
      for i in range(len(nums) - 1):
          if nums[i] > nums[i + 1]:
              nums[i], nums[i + 1] = nums[i + 1], nums[i]
              loop = True
  return nums


test_arr = [5,2,3,1]
print(bubbleSort(test_arr))


a = "abc2"
print(a == "abc")



