from collections import deque
def compute_max(a,k):
	q=deque()
	for i in range(k):
	    if(len(q)==0 or a[q[-1]]>=a[i]):
	        q.append(i)
	    else:
	        while(len(q)!=0 and a[q[-1]]<a[i]):
	            q.pop()
	        q.append(i)
	ans=[]
	ans.append(a[q[0]])
	for i in range(k,len(a)):
	    if(len(q)==0 or a[q[-1]]>=a[i]):
	        q.append(i)
	    else:
	        while(len(q)!=0 and a[q[-1]]<a[i]):
	            q.pop()
	        q.append(i)
	    while(len(q)!=0 and q[0]<=i-k):
	        q.popleft()
	    ans.append(a[q[0]])
	return ans
def compute_min(a,k):
	q=deque()
	for i in range(k):
	    if(len(q)==0 or a[q[-1]]<=a[i]):
	        q.append(i)
	    else:
	        while(len(q)!=0 and a[q[-1]]>a[i]):
	            q.pop()
	        q.append(i)
	ans=[]
	ans.append(a[q[0]])
	for i in range(k,len(a)):
	    if(len(q)==0 or a[q[-1]]<=a[i]):
	        q.append(i)
	    else:
	        while(len(q)!=0 and a[q[-1]]>a[i]):
	            q.pop()
	        q.append(i)
	    while(len(q)!=0 and q[0]<=i-k):
	        q.popleft()
	    ans.append(a[q[0]])
	return ans
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, a, k):
        max_arr=compute_max(a,k)
        min_arr=compute_min(a,k)
        ans=0
        for x,y in zip(max_arr,min_arr):
            ans=(ans+x+y)%(10**9+7)
        return ans
"""
Sum of min and max
Problem Description

Given an array A of both positive and negative integers.

Your task is to compute sum of minimum and maximum elements of all sub-array of size B.

NOTE: Since the answer can be very large, you are required to return the sum modulo 109 + 7.



Problem Constraints
1 <= size of array A <= 105

-109 <= A[i] <= 109

1 <= B <= size of array



Input Format
The first argument denotes the integer array A.
The second argument denotes the value B



Output Format
Return an integer that denotes the required value.



Example Input
Input 1:

 A = [2, 5, -1, 7, -3, -1, -2]
 B = 4
Input 2:

 A = [2, -1, 3]
 B = 2


Example Output
Output 1:

 18
Output 2:

 3


Example Explanation
Explanation 1:

 Subarrays of size 4 are : 
    [2, 5, -1, 7],   min + max = -1 + 7 = 6
    [5, -1, 7, -3],  min + max = -3 + 7 = 4      
    [-1, 7, -3, -1], min + max = -3 + 7 = 4
    [7, -3, -1, -2], min + max = -3 + 7 = 4   
    Sum of all min & max = 6 + 4 + 4 + 4 = 18 
Explanation 2:

 Subarrays of size 2 are : 
    [2, -1],   min + max = -1 + 2 = 1
    [-1, 3],   min + max = -1 + 3 = 2
    Sum of all min & max = 1 + 2 = 3
"""