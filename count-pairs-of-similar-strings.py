class Solution:
    def similarPairs(self, words: List[str]) -> int:

        return  sum(n*(n-1) for n in Counter([tuple(sorted(set(w)))
                    for w in words]).values())//2
