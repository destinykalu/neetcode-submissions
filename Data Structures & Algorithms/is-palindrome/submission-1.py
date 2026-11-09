class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.lower()#makes all character lowercase in the string
        p1=0 #first pointer at index 0 
        p2= len(s)-1 #second pointer at the end

        while p1<p2: #no overlap
            if not s[p1].isalnum(): #checks if character is alphanumeric a-z skips spaces dashes...
                p1 +=1 #update pointer
                continue #skip the rest of commands in loop
            if not s[p2].isalnum():
                p2 -=1
                continue
            if s[p1]==s[p2]:
                p1 +=1
                p2 -=1
           
            else:
                return False
        return True
                

