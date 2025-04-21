"""
Difficulty: [Easy]
NeetCode #: [4/250]
Date Solved: [21/04/25]
Attempt: [First Attempt]
Revision: 0

Approach:
- Find the difference between target and the number in the array. Use hashmaps to the record the number with its array index (val: index) you passed in an array.
when you find the diff, check if the number is in the hashmap. 

Time Complexity: O(n)
Space Complexity: O(n)

Key Insights:
- Find the difference and save in it in hashmaps.
"""

"""
Difficulty: [Easy]
NeetCode #: [3/250]
Date Solved: [18/04/25]
Attempt: [First Attempt]
Revision: 0

Problem Description:
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Examples:

Example 1:

Input: s = "racecar", t = "carrace"

Output: true

Example 2:

Input: s = "jar", t = "jam"

Output: false

Constraints:

s and t consist of lowercase English letters.

Approach:
Add characters from both arrays into through own hashmaps and compare them.

Time Complexity: O(n + m)
Space Complexity: O(1) Because we are at most using 26 characters only.

Key Insights:
- Using hashmaps for both the arrays
- Space can be O(1) when there is going to be limited number of space. Example, if string is "sssssssssssssssz", it only going to take up 2 space on hashmap.
"""

def twoSum(self, nums, target: int):
    prevMap = {} # val: index

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[nums[i]] = i
