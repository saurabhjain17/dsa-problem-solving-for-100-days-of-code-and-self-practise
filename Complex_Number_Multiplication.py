''' question:  A complex number can be represented as a string on the form "real+imaginaryi" where:

real is the real part and is an integer in the range [-100, 100].
imaginary is the imaginary part and is an integer in the range [-100, 100].
i2 == -1.
Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.

 

Example 1:

Input: num1 = "1+1i", num2 = "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:

Input: num1 = "1+-1i", num2 = "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
 

Constraints:

num1 and num2 are valid complex numbers.





LINK:-  https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/616/week-4-august-22nd-august-28th/3917/
'''



class Solution:
    def seperate(self,num):
        re1=""
        s1=1
        i1=0  
        i=0
        if num[0]=="+" or num[0]=="-":
            i=1 
            re1=num[0]
        while num[i]!="+" and  num[i]!="-" and i<len(num):
            re1+=num[i]
            i+=1
        if num[i]=="-":
                s1=-1
        re1=int(re1)
        i1=int(num[i+1:-1])
        return re1,s1,i1           

    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        re1,s1,i1=self.seperate(num1)
        re2,s2,i2=self.seperate(num2)
        re3=(re1*re2) +(s1*i1*s2*i2*-1)
        i3=re1*s2*i2+re2*s1*i1
        
        return(str(re3)+"+"+str(i3)+"i")
       


    