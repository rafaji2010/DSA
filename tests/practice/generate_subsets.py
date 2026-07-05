def generate_subsets_debug(arr, depth=0):
    indent = "  " * depth
    print(f"{indent}generate_subsets({arr})")
    
    if not arr:
        print(f"{indent}  BASE CASE → return [[]]")
        return [[]]
    
    first = arr[0]
    rest = generate_subsets_debug(arr[1:], depth + 1)
    
    print(f"{indent}  first={first}, rest={rest}")
    
    # Generate subsets WITH first element
    with_first = [[first] + subset for subset in rest]
    result = rest + with_first
    
    print(f"{indent}  → return {result}")
    return result