
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1= [0]*26
        count2 =[0]*26

        if len(s)!=len(t):
            return False
        for char in s:
            count1[ord(char)-ord('a')] +=1
        for char in t:
            count2[ord(char)-ord('a')] +=1
        if count1 == count2:
            return True
        return False


