# eval/lc_207_course_schedule.py
from typing import List
from collections import deque, defaultdict

def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """
    LeetCode 207: Course Schedule
    Detect cycle using Kahn's Algorithm (Topological Sort).
    Time: O(V + E) | Space: O(V + E)
    """
    # Build adjacency list and in-degree array
    adj_list = defaultdict(list)
    in_degree = [0] * num_courses
    
    for course, prereq in prerequisites:
        adj_list[prereq].append(course)
        in_degree[course] += 1
        
    # Queue for courses with 0 prerequisites
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    courses_taken = 0
    
    while queue:
        current = queue.popleft()
        courses_taken += 1
        
        # Reduce in-degree of neighbors
        for neighbor in adj_list[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                
    # If we took all courses, no cycle exists
    return courses_taken == num_courses

if __name__ == "__main__":
    # Example 1: 0 -> 1 (Take 0, then 1). Should be True.
    print(f"Can finish 2 courses [[1,0]]: {can_finish(2, [[1, 0]])}")  # Expected: True
    
    # Example 2: 0 -> 1 and 1 -> 0 (Cycle!). Should be False.
    print(f"Can finish 2 courses [[1,0],[0,1]]: {can_finish(2, [[1, 0], [0, 1]])}")  # Expected: False