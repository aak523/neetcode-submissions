class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        sorted_and_cut = sorted(count.items(), key=lambda x: -x[1])[:k]
        return list(map(lambda y: y[0], sorted_and_cut))