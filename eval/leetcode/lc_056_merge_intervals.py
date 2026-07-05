# eval/lc_056_merge_intervals.py
from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    LeetCode 56: Merge Intervals
    Time: O(n log n) due to sorting | Space: O(n) for result list
    """
    if not intervals:
        return []
        
    # 1. Sort intervals by their start time
    intervals.sort(key=lambda x: x[0])
    
    # 2. Initialize result with the first interval
    merged: List[List[int]] = [intervals[0]]
    
    # 3. Iterate through the rest
    for current in intervals[1:]:
        last = merged[-1]
        
        # If current overlaps with last
        if current[0] <= last[1]:
            # Merge by extending the end of the last interval
            last[1] = max(last[1], current[1])
        else:
            # No overlap, add current to result
            merged.append(current)
            
    return merged

if __name__ == "__main__":
    input_intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(f"Input: {input_intervals}")
    print(f"Merged: {merge(input_intervals)}")  # Expected: [[1, 6], [8, 10], [15, 18]]
    
    input_intervals_2 = [[1,4],[4,5]]
    print(f"\nInput: {input_intervals_2}")
    print(f"Merged: {merge(input_intervals_2)}")  # Expected: [[1, 5]]