class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        reverse = ""
        for i in s:
            if i.isalnum():
                reverse = reverse + i
        return reverse == reverse[::-1]        

        