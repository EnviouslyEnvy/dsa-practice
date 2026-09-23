class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        from collections import defaultdict
        courses_to_prereqs = defaultdict(set)

        for course, prereq in prerequisites:
            courses_to_prereqs[course].add(prereq)

        result = []
        
        visiting = set()
        visited = set()
        # Same as checking if it's in the result already, but having a separate set can be faster from lookup times.

        # Need to start from a course w/o prereqs?
        # We can still start from a course with prereqs, but we want to return append the nodes in reverse order.
        # Ie when we hit something with no prereqs then we can 
        # can append all not in courses_to_prereqs.
        def dfs(course):
            nonlocal result
            
            if course in visited:
                return True
            elif course in visiting:
                return False
            
            visiting.add(course)


            # If the courses prereqs have already been satisfied, return True
        
            for prereq in courses_to_prereqs[course]:
                if dfs(prereq) == False:
                    result=[]
                    return False
            visiting.remove(course)
            
            visited.add(course)
            result.append(course)
            
        for course in range(numCourses):
            if dfs(course)==False:
                return []
        return result
            