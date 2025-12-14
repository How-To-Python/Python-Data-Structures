from utility import print_section_header, print_subsection_header
# =============================================================================
# 8. NESTED LISTS
# =============================================================================

def nested_lists():
    """Demonstrate working with nested lists."""
    print_section_header("8. WORKING WITH NESTED LISTS")
    
    print_subsection_header("Creating and Accessing Nested Lists")
    
    # 2D matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("2D Matrix:")
    for row in matrix:
        print("  ", row)
    
    # Accessing elements
    print(f"Element at [1][2]: {matrix[1][2]}")  # 6
    print(f"First row: {matrix[0]}")
    print(f"Last column: [matrix[i][-1] for i in range(len(matrix))]: {[matrix[i][-1] for i in range(len(matrix))]}")
    
    print_subsection_header("Nested List Operations")
    
    # Modify nested list
    matrix[1][1] = 99
    print("After modifying [1][1] to 99:")
    for row in matrix:
        print("  ", row)
    
    # Add row
    matrix.append([10, 11, 12])
    print("After adding new row:")
    for row in matrix:
        print("  ", row)
    
    # Add column (more complex)
    for row in matrix:
        row.append(0)
    print("After adding column of zeros:")
    for row in matrix:
        print("  ", row)
    
    print_subsection_header("Flattening Nested Lists")
    
    nested = [[1, 2], [3, 4, 5], [6], [7, 8, 9]]
    print("Nested list:", nested)
    
    # Method 1: List comprehension
    flat1 = [item for sublist in nested for item in sublist]
    print("Flattened (comprehension):", flat1)
    
    # Method 2: Using sum with empty list
    flat2 = sum(nested, [])
    print("Flattened (sum trick):", flat2)
    
    # Method 3: Using itertools.chain
    import itertools
    flat3 = list(itertools.chain.from_iterable(nested))
    print("Flattened (itertools):", flat3)

def matrix_operations():
    """Demonstrate matrix operations with nested lists."""
    print_subsection_header("Matrix Operations")
    
    # Matrix addition
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]
    
    print("Matrix A:")
    for row in matrix_a:
        print("  ", row)
    
    print("Matrix B:")
    for row in matrix_b:
        print("  ", row)
    
    # Element-wise addition
    result = [[matrix_a[i][j] + matrix_b[i][j] 
              for j in range(len(matrix_a[0]))] 
              for i in range(len(matrix_a))]
    
    print("A + B:")
    for row in result:
        print("  ", row)
    
    # Matrix transpose
    matrix = [[1, 2, 3], [4, 5, 6]]
    transposed = [[matrix[j][i] for j in range(len(matrix))] 
                  for i in range(len(matrix[0]))]
    
    print("Original matrix:")
    for row in matrix:
        print("  ", row)
    
    print("Transposed:")
    for row in transposed:
        print("  ", row)