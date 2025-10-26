class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        adj =[[]*numCourses for _ in range(numCourses)] 
        
        sett = set()
        done = [False]*numCourses

        for u,v in prerequisites:
            adj[u].append(v)
        

        def dfs(i):
            
            if done[i]:
                return True
            
            if adj[i]==[]:
                done[i]=True
                order.append(i)
                return True

            if i in sett:
                return False

            sett.add(i)
            for n in adj[i]:

                if not dfs(n):
                    return False
            sett.remove(i)
            done[i]=True
            order.append(i)    
            return True

        for i in range(numCourses):

            if not done[i]:
                if not dfs(i):
                    return []
        
        return order
