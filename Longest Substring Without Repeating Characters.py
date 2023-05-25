class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = []
        length = 0
        for char in s:
            if char in chars:
                chars = chars[chars.index(char) + 1:]
            chars.append(char)
            length = max(length, len(chars))
        return length   
