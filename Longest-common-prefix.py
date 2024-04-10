class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()

        first = strs[0]
        last = strs[-1]
        common_prefix = ""
        for i in range(len(first)):
            if first[i] == last[i]:
                common_prefix += first[i]
            else:
                break

        return common_prefix