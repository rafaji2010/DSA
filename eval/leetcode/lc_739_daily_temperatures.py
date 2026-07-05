# eval/lc_739_daily_temperatures.py
from typing import List

def daily_temperatures(temperatures: List[int]) -> List[int]:
    """
    LeetCode 739: Daily Temperatures
    Uses a Monotonic Decreasing Stack to find the next warmer day.
    Time: O(n) - Each index is pushed and popped at most once.
    Space: O(n) - For the stack.
    """
    n = len(temperatures)
    # Initialize answer array with 0s (default if no warmer day is found)
    answer = [0] * n
    stack: List[int]= []  # Stores INDICES, not temperatures
    
    for i, temp in enumerate(temperatures):
        # While stack is not empty AND current temp > temp at the index on top of the stack
        while stack and temp > temperatures[stack[-1]]:
            prev_index = stack.pop()
            answer[prev_index] = i - prev_index
            
        stack.append(i)
        
    return answer

if __name__ == "__main__":
    # Test Case 1
    temps1 = [73, 74, 75, 71, 69, 72, 76, 73]
    print(f"Input: {temps1}")
    print(f"Output: {daily_temperatures(temps1)}")  # Expected: [1, 1, 4, 2, 1, 1, 0, 0]
    
    # Test Case 2
    temps2 = [30, 40, 50, 60]
    print(f"\nInput: {temps2}")
    print(f"Output: {daily_temperatures(temps2)}")  # Expected: [1, 1, 1, 0]