class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        for i in s:
            if i !="]":
                st.append(i)
            else:
                res=""
                while st[-1]!="[":
                    res=st.pop()+res
                st.pop()
                k=""
                while st and st[-1].isdigit():
                    k=st.pop()+k
                st.append(int(k)*res)
        return "".join(st)
