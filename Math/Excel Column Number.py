"""
Excel Column Number
Problem Description
Given a column title as appears in an Excel sheet, return its corresponding column number.


Problem Constraints
1 <= length of the column title <= 5


Input Format
Input a string which represents the column title in excel sheet.


Output Format
Return a single integer which represents the corresponding column number.


Example Input
Input 1:
 AB
Input 2:
 ABCD
       


Example Output
Output 1:
 28
Output 2:
 19010
        


Example Explanation
Explanation 1:
 A -> 1
 B -> 2
 C -> 3
 ...
 Z -> 26
 AA -> 27
 AB -> 28

"""


def index(c):
    return ord(c)-ord("A")+1
class Solution:
	# @param A : string
	# @return an integer
	def titleToNumber(self, s):
	    s=list(s)
	    s=list(map(index,s))
	    ans=0
	    j=0
	    for i in range(len(s)-1,-1,-1):
	        ans+=s[j]*(26**i)
	        j+=1
	    return ans
	    

        



        

	        
