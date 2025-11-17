import re

class Solution:
    def isValid(self, code: str) -> bool:
        tag_pat = r"<(/?)([A-Z]{1,9})>"
        open_cdata = "<![CDATA["
        close_cdata = "]]>"
  
        stack = []
        first_tag_seen = False
        i, j = 0, len(code)
        while i <= j:
            s = code.find('<', i)
            if s == -1: break     # no more <
            e = code.find('>', s+1)
            if e == -1: return False # no matching > for the last <
            candidate = code[s:e+1]
            m = re.fullmatch(tag_pat, candidate)
            if m:
                tag = m.groups()[1]
                if m.groups()[0] == '': # opening tag
                    # first tag must start from 0
                    if not first_tag_seen and s != 0: return False
                    stack.append(tag)
                    first_tag_seen = True
                else: # closing tag
                    if not stack or stack[-1] != tag: return False
                    # last tag needs to reach the last char
                    if len(stack) == 1 and e != len(code)-1: return False 
                    stack.pop()
                i = e+1
            elif len(candidate) >= len(open_cdata) and candidate[:len(open_cdata)] == open_cdata:
                    k = code.find(close_cdata, s+len(open_cdata))
                    if k == -1: # no close_cdata
                        return False
                    i = k+len(close_cdata)
            else:
                return False
                        
        return not stack and first_tag_seen





        
