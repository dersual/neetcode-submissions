from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  
        groups = defaultdict(list) 
        for w in strs: 
            counts = [0] * 26 
            for ch in w: 
                counts[ord(ch) - ord('a')] += 1 
            groups[tuple(counts)].append(w) 
        return list(groups.values())


        