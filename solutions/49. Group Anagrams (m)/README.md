## Group Anagrams
[LeetCode Problem](https://leetcode.com/problems/group-anagrams/description/)

## Problem Description
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

## My solution
1. Create a hash map where keys are canonical forms and values are lists of original strings
2. if the key is not in dictionary add the sorted value as key ("aet") and all associted value with it ["ate","eat","tea"]
3. Return only the values

