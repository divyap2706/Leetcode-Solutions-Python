class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap={i:[] for i in range(numCourses)} #creating adjacency list
        for crs,pre in prerequisites:
            preMap[crs].append(pre) #appending pre for DFS

        visitSet=set() #set of all visited nodes
        def dfs(crs):
            if crs in visitSet: #if the set is already visited, meaning its a cycle
                return False
            if preMap[crs]==[]: #if preMap of the course is empty, meaning it can be completed
                return True

            visitSet.add(crs)
            for pre in preMap[crs]:# run dfs for every prerequisite of the course
                if not dfs(pre):
                    return False
            visitSet.remove(crs)  #already visited the course so remove it
            preMap[crs]=[] #set the preMap empty to understand that the course can be completed
            return True

        for crs in range(numCourses): #calling DFS for all courses in a loop just in case of disconnected graphs(1->2 3->4)
            if not dfs(crs):
                return False
        return True
                
