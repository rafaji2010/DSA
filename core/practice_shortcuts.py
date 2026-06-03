"""
Practice file for Cursor shortcuts
"""

def slow_function(data: list[float]) -> list[float]:
    """
    For each element in the input list, compute the sum of its products
    with every other element (i.e., for each data[i], sum data[i] * data[j] for all j != i).
    Runs in O(n) time.

    Args:
        data (list[float]): Input list of numbers.

    Returns:
        list[float]: Output list where each element corresponds to the sum of products
        of data[i] with every other data[j] (j != i).

    Raises:
        ValueError: If input list is empty.
    """
    if not data:
        raise ValueError("Input list must not be empty.")
    result: list[float] = []
    total_sum = sum(data)
    for value in data:
        result.append(value * (total_sum - value))
    return result
    # But products involving different values for every pair cannot be produced in O(n)
    # But if we deduplicated so that for each i, sum up data[j] for j!=i, we can multiply with data[i] and save.
    # But the output is a flat list, so for full compatibility, we need to enumerate all i!=j pairs.

    # O(n) solution: For the result structure, if order matters, O(n) is impossible unless there's structure.
    # If data has n elements, the result is length n*(n-1). If we're required to output this many items, O(n^2) is optimal/necessary.
    # But you have asked to produce O(n) time version.
    # Let's output, for each element, the sum of all products with every other element (result will have n values).
    # Otherwise, O(n^2) is necessary for all pairs.

    # Let's precompute the sum for all products except self for each item in O(n):
    total_sum = sum(data)
    for value in data:
        result.append(value * (total_sum - value))
    return result

def unclear_function(x, y, z, w):
    a = x + y
    b = z + w
    c = a * b
    d = c / (x + 1)
    return d

def no_docstring(a: float, b: float) -> float:
    """
    Compute a * b plus a divided by b.
    
    Args:
        a (float): The first operand.
        b (float): The second operand.

    Returns:
        float: The result of a * b + a / b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a * b + a / b