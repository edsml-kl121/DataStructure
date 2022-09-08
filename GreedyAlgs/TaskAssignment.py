def taskAssignment(k, tasks):
    # Write your code here.
    indicies_task = getTaskindices(tasks)
    sorted_task = sorted(tasks) # o(n log n)
    left = 0
    right = len(tasks) - 1
    work_allocation = []
    while left < right:
        left_indx = indicies_task[sorted_task[left]]
        task1_indx = left_indx.pop()
        right_indx = indicies_task[sorted_task[right]]
        task2_indx = right_indx.pop()
        work_allocation.append([task1_indx, task2_indx])
        left += 1
        right -= 1
    return work_allocation

def getTaskindices(tasks):
    task_indicies = {}
    for index, taskDuration in enumerate(tasks):
        if taskDuration in task_indicies:
            task_indicies[taskDuration].append(index)
        else:
            task_indicies[taskDuration] = [index]
    return task_indicies

k =  3
tasks =  [1, 3, 5, 3, 1, 4]
print(taskAssignment(k, tasks))

