from utility import print_section_header, print_subsection_header, run_example, pause_for_user
# =============================================================================
# ADVANCED TECHNIQUES
# =============================================================================

def advanced_techniques():
    """Demonstrate advanced list techniques."""
    print_section_header("7. ADVANCED TECHNIQUES")
    
    print_subsection_header("Tuple Unpacking with Lists")
    
    # Unpacking coordinates
    coordinates = [(10, 20), (30, 40), (50, 60)]
    print("Coordinate pairs:", coordinates)
    
    print("Unpacked coordinates:")
    for x, y in coordinates:
        print(f"  Point: ({x}, {y})")
    
    # Unpacking with enumerate
    colors = ["red", "green", "blue"]
    print("Enumerate with unpacking:")
    for index, color in enumerate(colors):
        print(f"  Color {index + 1}: {color}")
    
    print_subsection_header("List Wrapping Technique")
    
    # Single category data
    category_names = ["Fruits"]
    category_items = ["apple", "banana", "orange"]
    
    print("Category names:", category_names)
    print("Category items:", category_items)
    
    # Without list wrapping (problematic)
    print("❌ Without list wrapping:")
    for name, item in zip(category_names, category_items):
        print(f"  {name}: {item}")  # Only pairs first elements
    
    # With list wrapping (correct)
    print("✅ With list wrapping:")
    for name, items in zip(category_names, [category_items]):
        print(f"  {name}: {', '.join(items)}")
    
    print_subsection_header("Extended Unpacking with Asterisk")
    
    # Unpacking with *
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    first, *middle, last = numbers
    print(f"First: {first}")
    print(f"Middle: {middle}")
    print(f"Last: {last}")
    
    # Head and tail
    head, *tail = numbers
    print(f"Head: {head}")
    print(f"Tail: {tail}")
    
    # Multiple assignments
    *beginning, second_last, last = numbers
    print(f"Beginning: {beginning}")
    print(f"Second last: {second_last}")
    print(f"Last: {last}")

def list_manipulation_advanced():
    """Demonstrate advanced list manipulation."""
    print_subsection_header("Advanced List Manipulation")
    
    # List rotation
    original = [1, 2, 3, 4, 5]
    print("Original list:", original)
    
    # Rotate left by 2 positions
    rotated_left = original[2:] + original[:2]
    print("Rotated left by 2:", rotated_left)
    
    # Rotate right by 2 positions  
    rotated_right = original[-2:] + original[:-2]
    print("Rotated right by 2:", rotated_right)
    
    # Chunking a list
    data = list(range(1, 21))  # [1, 2, 3, ..., 20]
    chunk_size = 5
    
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
    print(f"Original data: {data}")
    print(f"Chunks of {chunk_size}:")
    for i, chunk in enumerate(chunks):
        print(f"  Chunk {i + 1}: {chunk}")
    
    # Remove duplicates while preserving order
    with_duplicates = [1, 2, 3, 2, 4, 3, 5, 1, 6]
    unique_ordered = []
    seen = set()
    for item in with_duplicates:
        if item not in seen:
            unique_ordered.append(item)
            seen.add(item)
    
    print("With duplicates:", with_duplicates)
    print("Unique ordered:", unique_ordered)


