class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pair = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            pair[key].append(word)
        return list(pair.values())