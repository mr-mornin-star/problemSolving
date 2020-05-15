"""
Reverse Bits
Problem Description
Reverse the bits of an 32 bit unsigned integer A.


Problem Constraints
0 <= A <= 232
    


Input Format
First and only argument of input contains an integer A.


Output Format
Return a single unsigned integer denoting minimum xor value.


Example Input
Input 1:
 0
Input 2:
 3
     


Example Output
Output 1:
 0
Output 2:
 3221225472
     


Example Explanation
Explanation 1:
        00000000000000000000000000000000    =>      00000000000000000000000000000000
Explanation 2:      
        00000000000000000000000000000011    =>      11000000000000000000000000000000

"""


class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, n):
        n=list(bin(n).replace("0b",""))
        # n=list(n)
        n.reverse()
        
        arr=["0"]*32
        for i in range(len(n)):
            arr[i]=n[i]
        # print(len(arr))
        arr="".join(arr)
        arr=int(arr,2)
        return arr

        

	        
