class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for ch in s:
            if ord('A')<=ord(ch)<=ord('z') or ord('0')<=ord(ch)<=ord('9'):
                string += ch.lower()
        print(string)
        for i in range(len(string)):
            if string[i] != string[-1-i]:
                return False
        return True

                