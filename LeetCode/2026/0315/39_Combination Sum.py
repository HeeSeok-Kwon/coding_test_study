class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        idx = 0
        result = []

        def dfs(selection, remaining_target, idx):
            for i in range(idx, len(candidates)):
                if(remaining_target < 0):
                    return
                elif(remaining_target == 0):
                    result.append(selection.copy())
                    return
                else:
                    selection.append(candidates[i])
                    dfs(selection,  remaining_target - candidates[i], i)
                    selection.pop()

        dfs([], target, idx)
        return result