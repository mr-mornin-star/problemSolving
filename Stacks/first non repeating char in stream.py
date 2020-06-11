from collections import deque
from collections import defaultdict
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, a):
        mem=defaultdict(int)
        q=deque()
        ans=[]
        for c in a:
            # print(q)
            # print(mem)
            if c not in mem:
                q.append(c)
            mem[c]+=1
            while(len(q)!=0 and mem[q[0]]>1):
                q.popleft()
            if(len(q)==0):
                ans.append("#")
            else:
                ans.append(q[0])
        # print(mem["h"])
        return "".join(ans)



"""
First non-repeating character
Problem Description

Given a string A denoting a stream of lowercase alphabets.

You have to make new string B. B is formed such that we have to find first non-repeating character each time a character is inserted to the stream and append it at the end to B. if no non-repeating character is found then append '#' at the end of B.



Problem Constraints
1 <= |A| <= 100000



Input Format
The only argument given is string A.



Output Format
Return a string B after processing the stream of lowercase alphabets A.



Example Input
Input 1:

 A = "abadbc"
Input 2:

 A = "abcabc"


Example Output
Output 1:

"aabbdd"
Output 2:

"aaabc#"


Example Explanation
Explanation 1:

"a"      -   first non repeating character 'a'
"ab"     -   first non repeating character 'a'
"aba"    -   first non repeating character 'b'
"abad"   -   first non repeating character 'b'
"abadb"  -   first non repeating character 'd'
"abadbc" -   first non repeating character 'd'
Explanation 2:

"a"      -   first non repeating character 'a'
"ab"     -   first non repeating character 'a'
"abc"    -   first non repeating character 'a'
"abca"   -   first non repeating character 'b'
"abcab"  -   first non repeating character 'c'
"abcabc" -   no non repeating character so '#'
"""