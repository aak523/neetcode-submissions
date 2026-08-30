class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)

        def listRepr(anagram: str) -> Tuple[int, ...]:
            occurrences = [0] * 26
            start_idx = ord('a')
            for c in anagram:
                occurrences[ord(c) - start_idx] += 1
            return tuple(occurrences)

        for s in strs:
            count[listRepr(s)].append(s)

        return list(count.values())
