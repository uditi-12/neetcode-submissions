class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            t = "".join(sorted(i))
            d[t].append(i)
        
        return list(d.values())