class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def dfs(i, cur, total):
            if total>target:
                return
            
            if total == target:
                result.append(cur.copy())
                return
            
            for nxt in range(i, len(candidates)):
                if nxt != i and candidates[nxt] == candidates[nxt-1]:
                    continue
                cur.append(candidates[nxt])
                dfs(nxt+1, cur, total+candidates[nxt])
                cur.pop()

        dfs(0,[],0)
        return result