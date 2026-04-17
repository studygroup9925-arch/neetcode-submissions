class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_str=min(strs,key=len)
        for i in range(len(shortest_str)):
            for s in strs:
                if s[i]!=shortest_str[i]:
                    return shortest_str[:i]
        return shortest_str