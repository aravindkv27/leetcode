nums = list(map(int, input().split()))

target = int(input())

hashset = {}

for i, n in enumerate(nums):

    difference = target - n

    if difference in hashset:

        print([hashset[difference], i])

    hashset[n] = i
