"""
Single Number III
Problem Description
Given an array of numbers A , in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. Note: Output array must be sorted.  


Problem Constraints
2 <= |A| <= 100000
1 <= A[i] <= 109


Input Format
First argument is an array of interger of size N.


Output Format
Return an array of two integers that appear only once.


Example Input
Input 1:
A = [1, 2, 3, 1, 2, 4]
  Input 2:      
A = [1, 2]
    


Example Output
Output 1:
[3, 4]
  Output 2:      
[1, 2]
    


Example Explanation
Explanation 1:
 3 and 4 appear only once.
  Explanation 2:      
 1 and 2 appear only once.

"""


import math as m 
def getIbit(n,i):
    return 1 if (n & (1<<i))!=0 else 0
 
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, a):
        xor_2=0
        for i in a:
            xor_2^=i
        xor_a=0
        xor_b=0
        index=0
        for i in range(int(m.log2(xor_2))):
            if getIbit(xor_2,i)==1:
                index=i
                break
        for num in a:
            if(getIbit(num,index)==1):
                xor_a^=num
            else:
                xor_b^=num
        ans=[xor_a,xor_b]
        ans.sort()
        return ans
        

	        
