class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str_first = strs[0]
        result = ""

        for i in range(0, len(str_first)):
            character = str_first[i]
            compare = True
            for j in range(1, len(strs)):
                if(len(strs[j]) <= i):
                    return result
                if(character != strs[j][i]):
                    compare = False
                    break

            if(compare):
                result += character
            else:
                break

        return result