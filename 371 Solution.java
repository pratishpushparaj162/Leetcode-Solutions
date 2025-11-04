class Solution:
    def getSum(self, a: int, b: int) -> int:
        l =[]
        c=0
        if a<0 and b<0:
            c=a
            a=int((a*a)/abs(a))
            b=int((b*b)/abs(b))
            for i in range(a):
                l.append(1)
            for i in range(b):
                l.append(1)
            a=c
            c=int(len(l)*a/abs(a))
            return c

        elif a<0 or b<0:
            if abs(b)>abs(a):
                c=a
                a=b
                b=c
            for i in range(abs(a)):
                l.append(1)
            for i in range(abs(b)):
                l.remove(1)
            c=len(l)
            if a<0:
                c = int(c*a/abs(a))
            return c
        else:
            for i in range(a):
                l.append(1)
            for i in range(b):
                l.append(1)

            return len(l)    
