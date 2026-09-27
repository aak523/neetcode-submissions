class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        occurrences = set(nums)
        longest = 0

        for num in occurrences:
            if num - 1 not in occurrences:
                length = 1
                while num + length in occurrences:
                    length += 1
                longest = max(length, longest)
        
        return longest