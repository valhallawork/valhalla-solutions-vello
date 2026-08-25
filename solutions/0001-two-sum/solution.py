from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to map the number to its index
        seen = {}
        
        for index, num in enumerate(nums):
            # Calculate the required pair value
            complement = target - num
            
            # Check if the complement has already been seen
            if complement in seen:
                return [seen[complement], index]
            
            # Store the current number and its index
            seen[num] = index
            
        return []

