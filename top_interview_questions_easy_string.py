"""
1. Reverse String

Write a function that reverses a string. 
The input string is given as an array of characters char[].

Do not allocate extra space for another array, 
you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""

def reverseString(s):
	return s[::-1]

"""
2. Reverse Integer

Note:
Assume we are dealing with an environment 
that could only store integers within the 
32-bit signed integer range: [−231,  231 − 1]. 

For the purpose of this problem, assume 
that your function returns 0 when the reversed integer overflows.

Example 1:

Input: x = 123
Output: 321
"""

def reverse(x):
	x = str(x)
	x = x[::-1]

	if x[-1] == '-':
		x = x[:-1]
		x = '-' + x

	x = int(x)

	if x >= 2**31-1 or x <= -2**31:
		return 0

	return x


"""
3. First Unique Character in a String

Given a string, find the first non-repeating character in it 
and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
"""

def firstUniqChar(s):
	result = []

	for i in set(s):
		if s.count(i) == 1:
			result.append(s.index(i))

	if len(result) > 0:
		return min(result)
	else:
		return -1

	return -1


"""
3. Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
"""

def isAnagram(s, t):
	return len(sorted(s)) == len(sorted(t))

"""
4. Valid Palindrome

Given a string, determine if it is a palindrome, 
considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, 
we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
"""

def isPalindrome(s):
	result = []

	for s in sentence:
		if s.isalpha() or s.isnumeric():
			result.append(s.lower())

	if result == result[::-1]:
		return True

	return False


"""
5. String to Integer (atoi)

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters
as necessary until the first non-whitespace character is found. 
Then, starting from this character takes an optional initial plus 
or minus sign followed by as many numerical digits as possible,
and interprets them as a numerical value.

The string can contain additional characters 
after those that form the integral number, 
which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters 
in str is not a valid integral number, 
or if no such sequence exists because either str is empty or 
it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered a whitespace character.
Assume we are dealing with an environment that 
could only store integers within 
the 32-bit signed integer range: [−231,  231 − 1]. 
If the numerical value is out of the range of representable values, 
231 − 1 or −231 is returned.

Example 1:

Input: str = "42"
Output: 42

Example 3:

Input: str = "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' 
as the next character is not a numerical digit.
"""

def myAtoi(s):
	str = str.strip()
	str = re.findall('(^[\+\-0]*\d+)\D*', str)

	try:
		result = int(''.join(str))
		max_int = 2147483647
		min_int = -2147483648
		if result > max_int > 0:
			return max_int
		elif result < min_int < 0:
			return min_int
		else:
			return result
	except:
		return 0


"""
6. Implement strStr()

Implement strStr().

Return the index of the first occurrence 
if needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
"""

def strStr(haystack, needle):
	for i in range(len(haystack)):
		if haystack[i:i+len(needle)] == needle:
			return i

	return -1


"""
7. Count and Say

The count-and-say sequence is a sequence of digit strings 
defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" 
the digit string from countAndSay(n-1), 
which is then converted into a different digit string.

Example 2:

Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
"""

def countAndSay(n):
	s = '1'
	for _ in range(n-1):
		let = s[0]
		temp = ''
		count = 0

		for l in s:
			if let == l:
				count += 1
			else:
				temp += str(count)+let
				let = l
				count = 1

		temp += str(count)+let
		s = temp

	return s


"""
8. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
"""

def longestCommonPrefix(strs):
	if not strs: 
		return ""
	if len(strs) == 1: 
		return strs[0]

	strs = sorted(strs)
	common = []

	for i, j in zip(strs[0], strs[-1]):
		if i == j:
			common.append(i)
		else:
			break

	return ''.join(common)