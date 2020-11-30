"""
1. Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates 
in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, 
you must do this by modifying the input array in-place with O(1) extra memory.

Input: nums = [1,1,2]
Output: 2, nums = [1,2]
Explanation: Your function should return length = 2,
with the first two elements of nums being 1 and 2 respectively. 
It doesn't matter what you leave beyond the returned length.
"""
def removeDuplicates(nums):
	return len(set(nums))


# Using pointer
def removeDuplicates_pointer(nums):
    i = 0
    j = 0
    
    for j in range(len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


"""
2. Best Time to Buy and Sell Stock II

Say you have an array prices for which the 
ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
"""

def maxProfit(prices):
	profit = 0
	result = []

	for price in range(len(prices) - 1):
	    if prices[price] < prices[price + 1]:
	        profit = prices[price + 1] - prices[price]
	        result.append(profit)
	        
	return sum(result)


"""
3. Rotate Array

Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, 
there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""

# This is not in-place
def rotate(nums, k):
	j = len(nums)

	return nums[j-k:] + nums[:j-k]

# In-place solution
def rotate_inplace(nums, k):
	k %= len(nums)

	nums[:] = nums[-k:] + nums[:-k]

"""
4. Conatains Duplicate

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears
at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
"""

def containsDuplicate(nums):
	if len(nums) == len(set(nums)):
		return True
	return False


"""
5. Single Number

Given a non-empty array of integers nums, 
every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with 
a linear runtime complexity and without using extra memory?

Example 1:

Input: nums = [2,2,1]
Output: 1
"""
def singleNumber(nums):
	lst = []

	for num in nums:
		if num not in lst:
			lst.append(num)
		else:
			lst.remove(num)

	return lst.pop()

# Using XOR
def singleNumber_xor(nums):
	res = 0
	for num in nums:
		res ^= num
	return res


"""
6. Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
"""

def intersect(nums1, nums2):
    nums1, nums2 = sorted(nums1), sorted(nums2)
    ptr1 = ptr2 = 0
    result = []
    
    while True:
        try:
            if nums1[ptr1] > nums2[ptr2]:
                ptr2 += 1
            elif nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1
            else:
                result.append(nums1[ptr1])
                ptr1 += 1
                ptr2 += 1
        except IndexError:
            break
    
    return result


"""
7. Plus One

Given a non-empty array of decimal digits 
representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is 
at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, 
except the number 0 itself.

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
"""

def plusOne(digits):
	number = int(''.join(str(digit) for digit in digits))

	number += 1
	number = str(number)
	new = [int(num) for num in number]

	return new


"""
8. Move Zeroes

Given an array nums, write a function to move all 0's to 
the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

def moveZeroes(nums):
	i = j = 0

	while j < len(nums):
		if nums[j] != 0:
			nums[i], num[j] = nums[j], nums[i]
			i += 1
		j += 1


"""
9. Two Sum
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

def twoSum(nums, target):
	storage = {}

	for idx, num in enumerate(nums):
		result = target - num

		if result in storage:
			return [storage[result], idx]

		else:
			storage[num] = idx


"""
10. Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. 
Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid
must contain the digits 1-9 without repetition.

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
"""

def isValidSudoku(board):
	seen = sum(([(c, i), (j, c), (i/3, j/3, c)]
		for i, row in enumerate(board)
		for j, c in enumerate(row)
		if c != '.'), [])

	return len(seen) == len(set(seen))

"""
11. Rotate Image

You are given an n x n 2D matrix representing an image, 
rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, 
which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
"""

def rotate(matrix):
	matrix.reverse()

	for i in range(len(matrix)):
		for j in range(i):
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(matrix)
matrix.reverse()

print(matrix)

for i in range(len(matrix)):
	for j in range(i):
		matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print(matrix)