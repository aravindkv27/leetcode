class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # input_val = input()

#         nums = json.loads(input_val)


        output_value = []
        sum = 0

        for i in range(0,len(nums)):

            sum = sum + int(nums[i])
            output_value.append(sum)

        # print(output_value)
        return output_value