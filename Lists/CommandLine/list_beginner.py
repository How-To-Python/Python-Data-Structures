from utility import print_section_header, print_subsection_header
# =============================================================================
# LIST BASICS
# =============================================================================

def list_basics():
    """Demonstrate list creation, access, and basic properties."""
    print_section_header("1. LIST BASICS")
    
    print_subsection_header("Creating Lists")
    
    # Empty list
    empty_list = []
    print("Empty list:", empty_list)
    print("Type:", type(empty_list))
    
    # List with mixed data types
    mixed_list = [1, "hello", 3.14, True, None]
    print("Mixed data types:", mixed_list)
    
    # List from range
    numbers = list(range(1, 6))
    print("From range:", numbers)
    
    # List from string
    char_list = list("Python")
    print("From string:", char_list)
    
    print_subsection_header("Accessing Elements")
    
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    print("Fruits list:", fruits)
    
    # Positive indexing
    print("First fruit (index 0):", fruits[0])
    print("Third fruit (index 2):", fruits[2])
    
    # Negative indexing
    print("Last fruit (index -1):", fruits[-1])
    print("Second to last (index -2):", fruits[-2])
    
    print_subsection_header("List Properties")
    
    # Length
    print("Length of fruits:", len(fruits))
    
    # Check if item exists
    print("'apple' in fruits:", "apple" in fruits)
    print("'grape' in fruits:", "grape" in fruits)
    
    # Index of element
    print("Index of 'cherry':", fruits.index("cherry"))

def list_slicing_demo():
    """Demonstrate list slicing techniques."""
    print_subsection_header("List Slicing")
    
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Original list:", numbers)
    
    # Basic slicing
    print("First 5 elements [0:5]:", numbers[0:5])
    print("Elements 3 to 7 [3:8]:", numbers[3:8])
    print("Last 3 elements [-3:]:", numbers[-3:])
    print("All except last 2 [:-2]:", numbers[:-2])
    
    # Step slicing
    print("Every 2nd element [::2]:", numbers[::2])
    print("Every 3rd from index 1 [1::3]:", numbers[1::3])
    print("Reverse the list [::-1]:", numbers[::-1])

# =============================================================================
# BASIC OPERATIONS
# =============================================================================

def basic_operations():
    """Demonstrate basic list operations."""
    print_section_header("2. BASIC OPERATIONS")
    
    # Starting with a list
    colors = ["red", "green", "blue"]
    print("Starting list:", colors)
    
    print_subsection_header("Adding Elements")
    
    # append() - add single element to end
    colors.append("yellow")
    print("After append('yellow'):", colors)
    
    # insert() - add element at specific position
    colors.insert(1, "orange")
    print("After insert(1, 'orange'):", colors)
    
    # extend() - add multiple elements
    colors.extend(["purple", "pink"])
    print("After extend(['purple', 'pink']):", colors)
    
    # + operator - concatenation
    more_colors = colors + ["black", "white"]
    print("Using + operator:", more_colors)
    
    print_subsection_header("Removing Elements")
    
    # remove() - remove first occurrence
    colors.remove("orange")
    print("After remove('orange'):", colors)
    
    # pop() - remove and return element
    last_color = colors.pop()
    print("Popped element:", last_color)
    print("List after pop():", colors)
    
    # pop(index) - remove element at index
    second_color = colors.pop(1)
    print("Popped element at index 1:", second_color)
    print("List after pop(1):", colors)
    
    # del - delete element or slice
    del colors[0]
    print("After del colors[0]:", colors)
    
    # clear() - remove all elements
    temp_list = colors.copy()
    temp_list.clear()
    print("After clear():", temp_list)
    
    print_subsection_header("Modifying Elements")
    
    # Direct assignment
    colors[0] = "crimson"
    print("After colors[0] = 'crimson':", colors)
    
    # Slice assignment
    colors[1:3] = ["navy", "gold"]
    print("After slice assignment:", colors)