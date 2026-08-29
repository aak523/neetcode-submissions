class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        start_idx = ord('a')
        for i in range(len(s)):
            count[ord(s[i]) - start_idx] += 1
            count[ord(t[i]) - start_idx] -= 1

        for val in count:
            if val != 0:
                return False
        return True