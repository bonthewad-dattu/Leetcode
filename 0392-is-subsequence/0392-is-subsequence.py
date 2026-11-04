class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        str3 =''
        index = 0
        for i in range(len(s)):
            is_true = False
            for j in range(index,len(t)):
                if s[i] == t[j]:
                    str3 = str3 + t[j]

                    index = j + 1
                    is_true = True
                    break
            if not is_true:
                break        
        return s == str3            
        