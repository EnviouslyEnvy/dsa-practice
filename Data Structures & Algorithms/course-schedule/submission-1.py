class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # We need to find if this graph contains a cycle.
        # I think we can assume that we can take any course that appears as a prerequisite, without having a prerequisite itself.
        from collections import defaultdict
        # This will map a course to its prereqs
        # If we have {a:(b)} we should check if b: (...) contains a
        # We can eventually check if within courseToPrereqs[course_a] in
        # No wait, this only works if they are directly cyclical.
        # I'm silly we just need to check if we visited a node before in a singular traversal. i think.
        # Record the nodes traversed
        visited = set()
        
        course_to_prereqs = defaultdict(set)

        for course, prereq in prerequisites:
            course_to_prereqs[course].add(prereq)
        
        def dfs(course):
            if course in visited:
                return False
            
            if course_to_prereqs[course] == []:
                return True
            visited.add(course)
            for prereq in course_to_prereqs[course]:
                if dfs(prereq)==False:
                    return False
            visited.remove(course)
            course_to_prereqs[course]=[]
            # Since we have no issues with prereqs of this course we can simply set it to have no prereqs to make computing faster and take less repetitive recursion.
            return True
        
        for course in range(numCourses):
            if dfs(course)==False:
                return False
        
        return True

