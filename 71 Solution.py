class Solution:
    def simplifyPath(self, path: str) -> str:
        dir_list = [x for x in path.split('/') if x]
        l = len(dir_list)
        output = []
        skip = 0
        for i in range(l - 1, -1, -1):
            s = dir_list[i]
            if s == "..":
                skip += 1
            elif s == ".":
                pass
            else:
                if skip > 0:
                    skip -= 1
                else:
                    output.insert(0, s)
        return "/" + "/".join(output)
