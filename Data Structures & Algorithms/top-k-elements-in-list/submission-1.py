class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        d = Counter(nums)
        import heapq
        heap = []
        for i,f in d.items():
            heapq.heappush(heap,[f,i])
            if len(heap)>k:
                heapq.heappop(heap)
        return [nums for f, nums in heap]