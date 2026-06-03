"""
core/unsorted_experiment.py
Demonstrate why binary search requires sorted data
"""

import random

def binary_search(arr, target, verbose=False):
    """Binary search (requires sorted input)"""
    left, right = 0, len(arr) - 1
    steps = 0
    
    if verbose:
        print(f"\n  Searching for {target} in {arr}")
    
    while left <= right:
        steps += 1
        mid = (left + right) // 2
        
        if verbose:
            print(f"    Step {steps}: left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")
        
        if arr[mid] == target:
            if verbose:
                print(f"    ✓ FOUND at index {mid}!")
            return mid, steps
        elif arr[mid] < target:
            if verbose:
                print(f"    {target} > {arr[mid]} → search RIGHT half")
            left = mid + 1
        else:
            if verbose:
                print(f"    {target} < {arr[mid]} → search LEFT half")
            right = mid - 1
    
    if verbose:
        print(f"    ✗ NOT FOUND")
    return -1, steps


print("=" * 70)
print("WHY BINARY SEARCH NEEDS SORTED DATA")
print("=" * 70)

# Create an unsorted array
unsorted = [8, 2, 5, 1, 9, 3, 7, 4, 6]
print(f"\nUnsorted array: {unsorted}")

# Search for 7 (which exists at index 6)
print("\n" + "=" * 70)
print("CASE 1: Searching in UNSORTED array (WRONG!)")
print("=" * 70)

index, steps = binary_search(unsorted, 7, verbose=True)

print(f"\n❌ Binary search returned index {index}")
if index != -1:
    print(f"   Value at index {index} is {unsorted[index]}")
    if unsorted[index] == 7:
        print("   ✓ Wait, it worked? That's PURE LUCK!")
    else:
        print("   ✗ WRONG! Binary search found the wrong value!")

# Search for 1
print("\n" + "=" * 70)
print("CASE 2: Searching for 1 in UNSORTED array")
print("=" * 70)

index, steps = binary_search(unsorted, 1, verbose=True)

print(f"\n❌ Binary search returned index {index}")
if index != -1:
    print(f"   Value at index {index} is {unsorted[index]}")
    if unsorted[index] == 1:
        print("   ✓ Found correctly (but could have been wrong!)")
    else:
        print("   ✗ WRONG!")

# Now sort it
sorted_arr = sorted(unsorted)
print("\n" + "=" * 70)
print("CASE 3: Same array but SORTED (CORRECT!)")
print("=" * 70)
print(f"\nSorted array: {sorted_arr}")

index, steps = binary_search(sorted_arr, 7, verbose=True)
print(f"\n✅ Binary search returned index {index} (correct!)")
print(f"   Value at index {index} is {sorted_arr[index]} ✓")

print("\n" + "=" * 70)
print("MULTIPLE RUNS: DOES UNSORTED EVER WORK?")
print("=" * 70)

works_count = 0
fails_count = 0

for trial in range(20):
    # Create random unsorted array
    arr = list(range(10))
    random.shuffle(arr)
    target = random.choice(arr)
    
    bs_index, _ = binary_search(arr, target)
    ls_index = arr.index(target)
    
    if bs_index == ls_index:
        works_count += 1
        status = "✓"
    else:
        fails_count += 1
        status = "✗"
    
    print(f"{status} Trial {trial+1:2d}: Unsorted {arr} → Binary search found {target} at index {bs_index} (actual: {ls_index})")

print(f"\nResults: {works_count} correct, {fails_count} wrong out of 20 trials")
print(f"Success rate: {works_count/20*100}%")

print("\n" + "=" * 70)
print("CONCLUSION")
print("=" * 70)
print("""
Binary search on unsorted data:
❌ Does NOT guarantee correct results
❌ May return wrong index (if it finds something)
❌ May not find a value that exists
✓ Only works 100% of the time on SORTED arrays!

The sorted property is ESSENTIAL because:
   - It allows us to eliminate HALF the search space
   - Without sorting, the middle value tells us NOTHING
""")
