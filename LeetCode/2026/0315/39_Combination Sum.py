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
    
# input: [2,3,6,7], target: 7

# selection, target, i -> selection.append(candidates[i]), dfs(selection,  remaining_target - candidates[i], i)
# [], 7, 0 -> [2], dfs([2], 7-2, 0)
# [2], 5, 0 -> [2, 2], dfs([2, 2], 5-2, 0)
# [2, 2], 3, 0 -> [2, 2, 2], dfs([2, 2, 2], 3-2, 0)
# [2, 2, 2], 1, 0 -> [2, 2, 2, 2], dfs([2, 2, 2, 2], 1-2, 0)
# [2, 2, 2, 2], -1, 0 -> return (X)
# [2, 2, 2], 1, 1 -> [2, 2, 2, 3], dfs([2, 2, 2, 3], 1-3, 1)
# [2, 2, 2, 3], -1, 1 -> return (X)
# [2, 2, 2], 1, 2 -> [2, 2, 2, 6], dfs([2, 2, 2, 6], 1-6, 2)
# [2, 2, 2, 6], -5, 2 -> return (X)
# [2, 2, 2], 1, 3 -> [2, 2, 2, 7], dfs([2, 2, 2, 7], 1-7, 3)
# [2, 2, 2, 7], -6, 3 -> return (X)
# [2, 2], 3, 1 -> [2, 2, 3], dfs([2, 2, 3], 3-3, 1)
# [2, 2, 3], 0, 1 -> append -> return (O)
# [2, 2], 3, 2 -> [2, 2, 6], dfs([2, 2, 6], 3-6, 2)
# [2, 2, 6], -3, 2 -> return (X)
# [2, 2], 3, 3 -> [2, 2, 7], dfs([2, 2, 5], 3-7, 3)
# [2, 2, 7], -4, 3 -> return (X)
# [2, 3], 2, 1 -> [2, 3, 3], dfs([2, 3, 3], 2-3, 1)
# [2, 3, 3], -1, 1 -> return (X)
# [2, 3], 2, 2 -> [2, 3, 6], dfs([2, 3, 6], 2-6, 2)
# [2, 3, 6], -4, 2 -> return (X)
# [2, 3], 2, 3 -> [2, 3, 7], dfs([2, 3, 7], 2-7, 3)
# [2, 3, 7], -5, 3 -> return (X)
# ... 
