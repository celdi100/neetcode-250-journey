"""
Problem: [Contains Duplicate]
Difficulty: [Easy]
NeetCode #: [2/250]
Date Solved: [18/04/25]
Attempt: [First Attempt]
Revision: 0

Problem Description:
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Examples:

Input: nums = [1, 2, 3, 3]

Output: true

--

Input: nums = [1, 2, 3, 4]

Output: false

Approach:
Since it requires to check for duplicates, went with using hashmaps.

Time Complexity: O(n)
Space Complexity: O(n)

Key Insights:
- Using hashset over hashmaps
- Can sort first then check every next pair of numbers. improve time by O(n log n) but space is O (1) 
"""

def hasDuplicate(nums) -> bool:
    d = {}
    for n in nums:
        if n in d:
            return True
        else:
            d[n] = 1
    return False
         
        
        