from utility import print_section_header, print_subsection_header
# =============================================================================
# 6. LIST FUNCTIONS
# =============================================================================

def list_functions():
    """Demonstrate built-in functions that work with lists."""
    print_section_header("6. LIST FUNCTIONS")
    
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    prices = [29.99, 15.50, 45.00, 12.75, 67.25]
    
    print("Working with numbers:", numbers)
    print("Working with prices:", prices)
    
    print_subsection_header("Statistical Functions")
    
    # Basic statistics
    print(f"Length: {len(numbers)}")
    print(f"Maximum: {max(numbers)}")
    print(f"Minimum: {min(numbers)}")
    print(f"Sum: {sum(numbers)}")
    
    # Average calculation
    average = sum(numbers) / len(numbers)
    print(f"Average: {average:.2f}")
    
    print_subsection_header("Working with Strings")
    
    words = ["python", "programming", "is", "awesome", "and", "fun"]
    print("Words:", words)
    
    # String-specific operations
    print(f"Longest word: {max(words, key=len)}")
    print(f"Shortest word: {min(words, key=len)}")
    print(f"Total characters: {sum(len(word) for word in words)}")
    
    print_subsection_header("Type Checking and Conversion")
    
    mixed = [1, 2.5, "3", 4, "5.5"]
    print("Mixed list:", mixed)
    
    # Filter by type
    numbers_only = [x for x in mixed if isinstance(x, (int, float))]
    strings_only = [x for x in mixed if isinstance(x, str)]
    
    print("Numbers only:", numbers_only)
    print("Strings only:", strings_only)
    
    # Type conversion
    try:
        converted_numbers = [float(x) for x in mixed]
        print("All converted to float:", converted_numbers)
    except ValueError as e:
        print(f"Conversion error: {e}")
    
    print_subsection_header("All and Any Functions")
    
    # all() - check if all elements are truthy
    all_positive = [1, 2, 3, 4, 5]
    has_zero = [1, 2, 0, 4, 5]
    
    print(f"All positive numbers are truthy: {all(all_positive)}")
    print(f"List with zero - all truthy: {all(has_zero)}")
    
    # any() - check if any element is truthy
    all_zeros = [0, 0, 0]
    mixed_with_truth = [0, 0, 1, 0]
    
    print(f"Any element in all zeros is truthy: {any(all_zeros)}")
    print(f"Any element in mixed is truthy: {any(mixed_with_truth)}")
