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

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    return countS == countT
    # Alternative
    # for j in countS:
    #     if countS[j] != countT.get(j, 0):
    #         return False
    # return True
    
        