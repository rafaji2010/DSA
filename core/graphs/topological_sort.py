"""
core/graphs/topological_sort.py
Topological Sort using Kahn's Algorithm (BFS) and DFS
"""

from collections import deque, defaultdict
from typing import List, Dict, Set, Optional


def kahn_topological_sort(graph: Dict[int, List[int]]) -> Optional[List[int]]:
    """
    Kahn's Algorithm for Topological Sort (BFS-based).
    
    Time: O(V + E)
    Space: O(V)
    
    Algorithm:
    1. Calculate in-degree for each node
    2. Add nodes with in-degree 0 to queue
    3. Process queue: remove node, reduce neighbors' in-degree
    4. Add neighbors with in-degree 0 to queue
    5. If result length != number of nodes → cycle detected!
    """
    # Calculate in-degree for each node
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] = in_degree.get(neighbor, 0) + 1
    
    # Queue for nodes with in-degree 0
    queue = deque([node for node in graph if in_degree[node] == 0])
    
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check for cycle
    if len(result) != len(graph):
        return None  # Cycle detected
    
    return result


def kahn_topological_sort_trace(graph: Dict[int, List[int]]) -> Optional[List[int]]:
    """Kahn's Algorithm with detailed tracing"""
    print("\n" + "=" * 60)
    print("KAHN'S ALGORITHM (BFS-based Topological Sort)")
    print("=" * 60)
    
    # Calculate in-degree
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] = in_degree.get(neighbor, 0) + 1
    
    print(f"\nInitial in-degrees: {in_degree}")
    
    # Queue for nodes with in-degree 0
    queue = deque([node for node in graph if in_degree[node] == 0])
    print(f"Initial queue (in-degree 0): {list(queue)}")
    
    result = []
    step = 1
    
    while queue:
        node = queue.popleft()
        result.append(node)
        print(f"\nStep {step}: Remove {node}")
        
        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            print(f"  → Decrease in-degree of {neighbor} to {in_degree[neighbor]}")
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                print(f"    {neighbor} now has in-degree 0, added to queue")
        
        print(f"  Queue: {list(queue)}")
        print(f"  Result: {result}")
        step += 1
    
    if len(result) != len(graph):
        print("\n❌ CYCLE DETECTED! Not a DAG.")
        return None
    
    print(f"\n✅ Topological order: {result}")
    return result

def dfs_topological_sort(graph: Dict[int, List[int]]) -> Optional[List[int]]:
    """
    DFS-based Topological Sort.
    
    Time: O(V + E)
    Space: O(V)
    
    Algorithm:
    1. Perform DFS on each unvisited node
    2. After processing all neighbors, add node to stack
    3. Reverse stack for topological order
    """
    visited = set()
    stack = []
    temp = set()  # For cycle detection
    
    def dfs(node: int) -> bool:
        """DFS returns False if cycle detected"""
        if node in temp:
            return False  # Cycle detected!
        if node in visited:
            return True
        
        temp.add(node)
        
        for neighbor in graph.get(node, []):
            if not dfs(neighbor):
                return False
        
        temp.remove(node)
        visited.add(node)
        stack.append(node)
        return True
    
    for node in graph:
        if node not in visited:
            if not dfs(node):
                return None  # Cycle detected
    
    return stack[::-1]  # Reverse for topological order


def dfs_topological_sort_trace(graph: Dict[int, List[int]]) -> Optional[List[int]]:
    """DFS-based Topological Sort with tracing"""
    print("\n" + "=" * 60)
    print("DFS-BASED TOPOLOGICAL SORT")
    print("=" * 60)
    
    visited = set()
    stack = []
    temp = set()
    
    def dfs(node: int, depth: int = 0) -> bool:
        indent = "  " * depth
        print(f"{indent}dfs({node})")
        
        if node in temp:
            print(f"{indent}  ❌ CYCLE DETECTED at {node}!")
            return False
        
        if node in visited:
            print(f"{indent}  Already visited, skip")
            return True
        
        temp.add(node)
        print(f"{indent}  Processing neighbors of {node}: {graph.get(node, [])}")
        
        for neighbor in graph.get(node, []):
            if not dfs(neighbor, depth + 1):
                return False
        
        temp.remove(node)
        visited.add(node)
        stack.append(node)
        print(f"{indent}  ✓ Finished {node}, added to stack")
        print(f"{indent}  Stack: {stack}")
        return True
    
    for node in graph:
        if node not in visited:
            print(f"\nStarting DFS from node {node}")
            if not dfs(node):
                return None
    
    result = stack[::-1]
    print(f"\n✅ Topological order: {result}")
    return result

def has_cycle(graph: Dict[int, List[int]]) -> bool:
    """
    Detect if graph has a cycle using DFS.
    
    Time: O(V + E)
    """
    visited = set()
    recursion_stack = set()
    
    def dfs(node: int) -> bool:
        if node in recursion_stack:
            return True
        if node in visited:
            return False
        
        visited.add(node)
        recursion_stack.add(node)
        
        for neighbor in graph.get(node, []):
            if dfs(neighbor):
                return True
        
        recursion_stack.remove(node)
        return False
    
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    
    return False

def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """
    LeetCode 207 - Course Schedule
    
    Determines if all courses can be finished given prerequisites.
    This is a cycle detection problem in a directed graph!
    """
    # Build graph
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    
    return not has_cycle(graph)


def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    LeetCode 210 - Course Schedule II
    
    Returns the order of courses to take.
    """
    # Build graph
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    
    # Add all courses to graph (even with no edges)
    for i in range(num_courses):
        if i not in graph:
            graph[i] = []
    
    order = kahn_topological_sort(graph)
    return order if order else []

if __name__ == "__main__":
    print("=" * 60)
    print("TOPOLOGICAL SORT DEMONSTRATION")
    print("=" * 60)
    
    # Example 1: Valid DAG
    print("\n--- Example 1: Course Prerequisites ---")
    graph1 = {
        1: [2, 4],
        2: [3, 5],
        3: [],
        4: [5],
        5: []
    }
    print("Graph:", dict(graph1))
    
    result1 = kahn_topological_sort_trace(graph1)
    
    # Example 2: DFS-based
    result2 = dfs_topological_sort_trace(graph1)
    
    # Example 3: Graph with cycle
    print("\n" + "=" * 60)
    print("--- Example 2: Graph with CYCLE ---")
    print("=" * 60)
    
    graph_cycle = {
        1: [2],
        2: [3],
        3: [1]  # Cycle: 1 → 2 → 3 → 1
    }
    print("Graph with cycle:", dict(graph_cycle))
    
    result3 = kahn_topological_sort(graph_cycle)
    print(f"Topological sort returns: {result3} (None = cycle detected)")
    
    # Example 4: Cycle detection
    print("\n" + "=" * 60)
    print("--- Example 3: Cycle Detection ---")
    print("=" * 60)
    
    graph_no_cycle = {
        1: [2, 3],
        2: [4],
        3: [4],
        4: []
    }
    graph_cycle = {
        1: [2],
        2: [3],
        3: [1]
    }
    
    print(f"Graph has cycle? {has_cycle(graph_no_cycle)} (should be False)")
    print(f"Graph has cycle? {has_cycle(graph_cycle)} (should be True)")
    
    # Example 5: Course Schedule
    print("\n" + "=" * 60)
    print("--- Example 4: Course Schedule (LeetCode 207) ---")
    print("=" * 60)
    
    prerequisites = [[1, 0], [2, 1], [3, 2]]
    print(f"Prerequisites: {prerequisites}")
    print(f"Can finish? {can_finish(4, prerequisites)}")
    
    print("\n✅ Topological Sort complete!")