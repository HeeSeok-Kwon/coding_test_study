##### 풀이 1
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        result = False
        s_dict = {}

        for i in range(len(s)):
            if(s_dict.get(s[i]) is not None and s_dict.get(s[i]) != t[i]):
                return result
            else:
                s_dict[s[i]] = t[i]

        s_list = list(s_dict.values())
        s_set = set(s_list)

        if(len(s_list) == len(s_set)):
            result = True

        return result


##### 풀이 2
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        result = False
        s_to_t = {}
        t_to_s = {}

        for a, b in zip(s, t):
            s_mapped_t = s_to_t.get(a)
            t_mapped_s = t_to_s.get(b)

            if(s_mapped_t is not None):
                if(s_mapped_t == b):
                    pass
                else:
                    return result
            else:
                s_to_t[a] = b

            if(t_mapped_s is not None):
                if(t_mapped_s == a):
                    pass
                else:
                    return result
            else:
                t_to_s[b] = a

        if(len(s_to_t) == len(t_to_s)):
            result = True

        return result        