class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        for i in range(len(strs)):
            count = [0] * 26
            for j in range(len(strs[i])):
                count[ord(strs[i][j]) - ord("a")] += 1
            key = tuple(count)
            if key not in store:
                store[key] = [strs[i]]
            else:
                store[key].append(strs[i])
        return list(store.values())