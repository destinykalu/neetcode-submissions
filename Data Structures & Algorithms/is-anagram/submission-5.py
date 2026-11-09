
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        countS = {} 
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0) 
            countT[t[i]] = 1 + countT.get(t[i],0)

        return countS == countT 
        

" first check to see if the length of both strings are the same"
"create hashmaps for both strings" 
"since the legths are the same iterate over one of the strings "
"for each item creat a key value pair in the hash map. use .get to catch any error just in case the key hasnt yet been added"
"compare the two"

