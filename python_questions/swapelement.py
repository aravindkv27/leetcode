input_arr = list(map(int,input().split()))
pos1 = int(input())
pos2 = int(input())

# print(input_arr
# )

def swap_first_last(input_arr):

    input_arr[0], input_arr[-1] = input_arr[-1], input_arr[0]

    return input_arr

# print(swap_first_last(input_arr))

# swap two element in a list in the provided position

def swap_provided_position(input_arr, pos1,pos2):

    input_arr[pos1], input_arr[pos2] = input_arr[pos2], input_arr[pos1]

    return input_arr

print(swap_provided_position(input_arr,pos1-1,pos2-1))