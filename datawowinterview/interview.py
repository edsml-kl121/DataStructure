def find_triplets(input):
    # Your code goes here
    current_counter = 0
    tripplets = 0
    for i in range(0, len(input)):
        if current_counter == 0:
            print("here", current_counter)
            current_num = input[i]
            current_counter += 1
            print(current_num, input[i], current_counter)
        else:
            if current_num == input[i]:
                current_counter += 1
            else:
                current_counter = 1
                current_num = input[i]
            if current_counter == 3:
                tripplets += 1
                current_counter = 0

            print(current_num, input[i], current_counter)
    return tripplets

print(find_triplets([ 5, 5, 5, 5, 5, 5 ]))