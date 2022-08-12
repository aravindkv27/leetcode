class Solution:
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)-1
        while left <= right:
            
            val = left + (right - left) //2
            
            if target == nums[val]:
                
                return val
            
            # elif target != nums[val]:
            
                
            
            elif target > nums[val]:

                left = val + 1
            
            else:
                
                right = val - 1 
                
        return left
        