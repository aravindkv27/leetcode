class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, rig = 0, len(nums)-1
        
        while left <= rig:
            
            val = left + (rig - left)//2
            
            if nums[val] == target:
                return val
            elif target < nums[val]:
                rig = val - 1
            else:
                left = val +1
        return -1