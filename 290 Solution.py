class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        smap = {}
        pmap = {}

        str_list = s.split()
        pattern_list = list(pattern)

        if len(str_list) != len(pattern_list):
            return False

        for i in range(len(str_list)):
            if str_list[i] not in smap:
                smap[str_list[i]] = i

            if pattern_list[i] not in pmap:
                pmap[pattern_list[i]] = i
            
            if smap[str_list[i]] != pmap[pattern_list[i]]:
                return False

        return True

        # ==========
    def wordPattern1(self, pattern: str, s: str) -> bool:
        hmap = {}
        str_list = s.split()
        pattern_list = list(pattern)
        if len(str_list) != len(pattern_list):
            return 
            
        for let, word in zip(str_list, pattern_list):

            if let in hmap:
                if hmap[let] != word:
                    return False
            elif word in hmap.values():
                return False

            hmap[let] = word
        return True
