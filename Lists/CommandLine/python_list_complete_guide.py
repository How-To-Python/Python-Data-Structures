"""
COMPLETE GUIDE TO PYTHON LISTS
===============================

A comprehensive guide to working with Python lists, covering everything from basic operations
to advanced techniques with interactive examples and demonstrations.

This guide is responsive and includes hands-on examples that you can run to see the output.
"""

import sys
import os

def print_section_header(title, char="=", width=80):
    """Print a formatted section header."""
    print("\n" + char * width)
    print(f" {title} ".center(width, char))
    print(char * width)

def print_subsection_header(title, char="-", width=60):
    """Print a formatted subsection header."""
    print("\n" + char * width)
    print(f" {title} ")
    print(char * width)

def run_example(example_func):
    """Run an example function and handle any errors."""
    try:
        example_func()
    except Exception as e:
        print(f"❌ Error running example: {e}")

def pause_for_user():
    """Pause execution for user to review output."""
    input("\n🔍 Press Enter to continue to the next section...")

# =============================================================================
# TABLE OF CONTENTS
# =============================================================================

def show_table_of_contents():
    """Display the guide's table of contents."""
    print_section_header("PYTHON LISTS - COMPLETE GUIDE", "=")
    
    toc = """
📚 TABLE OF CONTENTS:

1. 📋 List Basics - Creation, Access, and Properties
2. 🔧 Basic Operations - Adding, Removing, and Modifying
3. 🔍 List Methods - Essential built-in methods  
4. 🎯 List Comprehensions - Powerful one-liner creations
5. 🔄 Iteration Techniques - Loops and advanced iteration
6. 📊 List Functions - Built-in functions (len, max, min, sum)
7. 🧩 Advanced Techniques - Slicing, unpacking, and more
8. 📦 Working with Nested Lists - Multi-dimensional data
9. 🚀 Performance Tips - Optimization and best practices
10. 🛠️ Real-World Examples - Practical applications
11. 🎮 Interactive Demonstrations - Hands-on practice
12. 📝 Quick Reference - Cheat sheet

Each section includes:
✅ Clear explanations
✅ Interactive code examples
✅ Output demonstrations
✅ Best practices
✅ Common pitfalls to avoid
    """
    print(toc)

# # =============================================================================
# # 1. LIST BASICS
# # =============================================================================

# def list_basics():
#     """Demonstrate list creation, access, and basic properties."""
#     print_section_header("1. LIST BASICS")
    
#     print_subsection_header("Creating Lists")
    
#     # Empty list
#     empty_list = []
#     print("Empty list:", empty_list)
#     print("Type:", type(empty_list))
    
#     # List with mixed data types
#     mixed_list = [1, "hello", 3.14, True, None]
#     print("Mixed data types:", mixed_list)
    
#     # List from range
#     numbers = list(range(1, 6))
#     print("From range:", numbers)
    
#     # List from string
#     char_list = list("Python")
#     print("From string:", char_list)
    
#     print_subsection_header("Accessing Elements")
    
#     fruits = ["apple", "banana", "cherry", "date", "elderberry"]
#     print("Fruits list:", fruits)
    
#     # Positive indexing
#     print("First fruit (index 0):", fruits[0])
#     print("Third fruit (index 2):", fruits[2])
    
#     # Negative indexing
#     print("Last fruit (index -1):", fruits[-1])
#     print("Second to last (index -2):", fruits[-2])
    
#     print_subsection_header("List Properties")
    
#     # Length
#     print("Length of fruits:", len(fruits))
    
#     # Check if item exists
#     print("'apple' in fruits:", "apple" in fruits)
#     print("'grape' in fruits:", "grape" in fruits)
    
#     # Index of element
#     print("Index of 'cherry':", fruits.index("cherry"))

# def list_slicing_demo():
#     """Demonstrate list slicing techniques."""
#     print_subsection_header("List Slicing")
    
#     numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     print("Original list:", numbers)
    
#     # Basic slicing
#     print("First 5 elements [0:5]:", numbers[0:5])
#     print("Elements 3 to 7 [3:8]:", numbers[3:8])
#     print("Last 3 elements [-3:]:", numbers[-3:])
#     print("All except last 2 [:-2]:", numbers[:-2])
    
#     # Step slicing
#     print("Every 2nd element [::2]:", numbers[::2])
#     print("Every 3rd from index 1 [1::3]:", numbers[1::3])
#     print("Reverse the list [::-1]:", numbers[::-1])

# # =============================================================================
# # 2. BASIC OPERATIONS
# # =============================================================================

# def basic_operations():
#     """Demonstrate basic list operations."""
#     print_section_header("2. BASIC OPERATIONS")
    
#     # Starting with a list
#     colors = ["red", "green", "blue"]
#     print("Starting list:", colors)
    
#     print_subsection_header("Adding Elements")
    
#     # append() - add single element to end
#     colors.append("yellow")
#     print("After append('yellow'):", colors)
    
#     # insert() - add element at specific position
#     colors.insert(1, "orange")
#     print("After insert(1, 'orange'):", colors)
    
#     # extend() - add multiple elements
#     colors.extend(["purple", "pink"])
#     print("After extend(['purple', 'pink']):", colors)
    
#     # + operator - concatenation
#     more_colors = colors + ["black", "white"]
#     print("Using + operator:", more_colors)
    
#     print_subsection_header("Removing Elements")
    
#     # remove() - remove first occurrence
#     colors.remove("orange")
#     print("After remove('orange'):", colors)
    
#     # pop() - remove and return element
#     last_color = colors.pop()
#     print("Popped element:", last_color)
#     print("List after pop():", colors)
    
#     # pop(index) - remove element at index
#     second_color = colors.pop(1)
#     print("Popped element at index 1:", second_color)
#     print("List after pop(1):", colors)
    
#     # del - delete element or slice
#     del colors[0]
#     print("After del colors[0]:", colors)
    
#     # clear() - remove all elements
#     temp_list = colors.copy()
#     temp_list.clear()
#     print("After clear():", temp_list)
    
#     print_subsection_header("Modifying Elements")
    
#     # Direct assignment
#     colors[0] = "crimson"
#     print("After colors[0] = 'crimson':", colors)
    
#     # Slice assignment
#     colors[1:3] = ["navy", "gold"]
#     print("After slice assignment:", colors)

# # =============================================================================
# # 3. LIST METHODS
# # =============================================================================

# def list_methods():
#     """Demonstrate essential list methods."""
#     print_section_header("3. LIST METHODS")
    
#     numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
#     print("Working with:", numbers)
    
#     print_subsection_header("Searching and Counting")
    
#     # count() - count occurrences
#     print("Count of 1:", numbers.count(1))
#     print("Count of 5:", numbers.count(5))
    
#     # index() - find first occurrence
#     print("Index of 4:", numbers.index(4))
#     print("Index of 5:", numbers.index(5))  # First occurrence
    
#     print_subsection_header("Sorting and Reversing")
    
#     # sort() - sort in place
#     numbers_copy = numbers.copy()
#     numbers_copy.sort()
#     print("Sorted (ascending):", numbers_copy)
    
#     numbers_copy.sort(reverse=True)
#     print("Sorted (descending):", numbers_copy)
    
#     # sorted() - return new sorted list
#     original = [3, 1, 4, 1, 5]
#     sorted_list = sorted(original)
#     print("Original:", original)
#     print("Sorted copy:", sorted_list)
    
#     # reverse() - reverse in place
#     letters = ['a', 'b', 'c', 'd']
#     print("Original letters:", letters)
#     letters.reverse()
#     print("After reverse():", letters)
    
#     print_subsection_header("Copying Lists")
    
#     # copy() - shallow copy
#     original = [1, 2, [3, 4]]
#     shallow = original.copy()
#     deep_copy = [item[:] if isinstance(item, list) else item for item in original]
    
#     print("Original:", original)
#     print("Shallow copy:", shallow)
    
#     # Demonstrate shallow vs deep copy
#     original[2].append(5)
#     print("After modifying nested list in original:")
#     print("Original:", original)
#     print("Shallow copy (affected):", shallow)

# # =============================================================================
# # 4. LIST COMPREHENSIONS
# # =============================================================================

# def list_comprehensions():
#     """Demonstrate list comprehensions."""
#     print_section_header("4. LIST COMPREHENSIONS")
    
#     print_subsection_header("Basic List Comprehensions")
    
#     # Basic syntax: [expression for item in iterable]
#     squares = [x**2 for x in range(1, 6)]
#     print("Squares of 1-5:", squares)
    
#     # String manipulation
#     words = ["hello", "world", "python"]
#     uppercase = [word.upper() for word in words]
#     print("Uppercase words:", uppercase)
    
#     # Working with existing list
#     numbers = [1, 2, 3, 4, 5]
#     doubled = [n * 2 for n in numbers]
#     print("Doubled numbers:", doubled)
    
#     print_subsection_header("Conditional List Comprehensions")
    
#     # With if condition
#     even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
#     print("Even squares 1-10:", even_squares)
    
#     # Conditional expression
#     signs = ["positive" if x > 0 else "negative" if x < 0 else "zero" 
#              for x in [-2, -1, 0, 1, 2]]
#     print("Number signs:", signs)
    
#     print_subsection_header("Working with Strings")
    
#     sentence = "Hello World Python Programming"
#     # Extract words longer than 5 characters
#     long_words = [word for word in sentence.split() if len(word) > 5]
#     print("Words longer than 5 chars:", long_words)
    
#     # Extract vowels from a string
#     text = "Python Programming"
#     vowels = [char for char in text.lower() if char in 'aeiou']
#     print("Vowels in text:", vowels)
    
#     print_subsection_header("Working with Dictionaries")
    
#     # From dictionary to list
#     student_grades = {"Alice": 95, "Bob": 87, "Charlie": 92, "Diana": 98}
    
#     # List of names
#     names = [name for name in student_grades.keys()]
#     print("Student names:", names)
    
#     # List of high grades
#     high_grades = [grade for grade in student_grades.values() if grade >= 90]
#     print("Grades >= 90:", high_grades)
    
#     # List of tuples
#     name_grade_pairs = [(name, grade) for name, grade in student_grades.items()]
#     print("Name-grade pairs:", name_grade_pairs)
    
#     # List of dictionaries with conditions
#     high_performers = [{"name": name, "grade": grade} 
#                       for name, grade in student_grades.items() 
#                       if grade >= 90]
#     print("High performers:", high_performers)

# def nested_list_comprehensions():
#     """Demonstrate nested list comprehensions."""
#     print_subsection_header("Nested List Comprehensions")
    
#     # Create a multiplication table
#     multiplication_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
#     print("5x5 Multiplication table:")
#     for row in multiplication_table:
#         print(row)
    
#     # Flatten a nested list
#     nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#     flattened = [item for sublist in nested for item in sublist]
#     print("Original nested:", nested)
#     print("Flattened:", flattened)
    
#     # Matrix transpose
#     matrix = [[1, 2, 3], [4, 5, 6]]
#     transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
#     print("Original matrix:", matrix)
#     print("Transposed:", transposed)

# # =============================================================================
# # 5. ITERATION TECHNIQUES
# # =============================================================================

# def iteration_techniques():
#     """Demonstrate various ways to iterate over lists."""
#     print_section_header("5. ITERATION TECHNIQUES")
    
#     fruits = ["apple", "banana", "cherry", "date"]
#     prices = [1.20, 0.50, 2.30, 3.00]
    
#     print_subsection_header("Basic Iteration")
    
#     # Simple for loop
#     print("Simple iteration:")
#     for fruit in fruits:
#         print(f"  - {fruit}")
    
#     print_subsection_header("Enumerate - Index and Value")
    
#     # enumerate() for index and value
#     print("With enumerate (index, value):")
#     for index, fruit in enumerate(fruits):
#         print(f"  {index}: {fruit}")
    
#     # enumerate with custom start
#     print("Enumerate with start=1:")
#     for index, fruit in enumerate(fruits, start=1):
#         print(f"  {index}. {fruit}")
    
#     print_subsection_header("Zip - Multiple Lists")
    
#     # zip() to iterate over multiple lists
#     print("Zip fruits and prices:")
#     for fruit, price in zip(fruits, prices):
#         print(f"  {fruit}: ${price:.2f}")
    
#     # zip with unequal lengths
#     colors = ["red", "yellow", "red"]  # shorter list
#     print("Zip with unequal lengths:")
#     for fruit, price, color in zip(fruits, prices, colors):
#         print(f"  {fruit} (${price:.2f}) - {color}")
    
#     print_subsection_header("Advanced Iteration")
    
#     # Iteration with conditions
#     print("Expensive fruits (> $2.00):")
#     for fruit, price in zip(fruits, prices):
#         if price > 2.00:
#             print(f"  {fruit}: ${price:.2f}")
    
#     # Iteration with enumerate and zip
#     print("Detailed fruit information:")
#     for index, (fruit, price) in enumerate(zip(fruits, prices), 1):
#         status = "Expensive" if price > 2.00 else "Affordable"
#         print(f"  {index}. {fruit}: ${price:.2f} ({status})")

# def range_and_indices():
#     """Demonstrate iteration using range and indices."""
#     print_subsection_header("Using Range and Indices")
    
#     numbers = [10, 20, 30, 40, 50]
    
#     # Traditional index-based iteration
#     print("Index-based iteration:")
#     for i in range(len(numbers)):
#         print(f"  Index {i}: {numbers[i]}")
    
#     # Reverse iteration using indices
#     print("Reverse iteration with indices:")
#     for i in range(len(numbers) - 1, -1, -1):
#         print(f"  Index {i}: {numbers[i]}")
    
#     # Step iteration
#     print("Every second element:")
#     for i in range(0, len(numbers), 2):
#         print(f"  Index {i}: {numbers[i]}")

# # =============================================================================
# # 6. LIST FUNCTIONS
# # =============================================================================

# def list_functions():
#     """Demonstrate built-in functions that work with lists."""
#     print_section_header("6. LIST FUNCTIONS")
    
#     numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
#     prices = [29.99, 15.50, 45.00, 12.75, 67.25]
    
#     print("Working with numbers:", numbers)
#     print("Working with prices:", prices)
    
#     print_subsection_header("Statistical Functions")
    
#     # Basic statistics
#     print(f"Length: {len(numbers)}")
#     print(f"Maximum: {max(numbers)}")
#     print(f"Minimum: {min(numbers)}")
#     print(f"Sum: {sum(numbers)}")
    
#     # Average calculation
#     average = sum(numbers) / len(numbers)
#     print(f"Average: {average:.2f}")
    
#     print_subsection_header("Working with Strings")
    
#     words = ["python", "programming", "is", "awesome", "and", "fun"]
#     print("Words:", words)
    
#     # String-specific operations
#     print(f"Longest word: {max(words, key=len)}")
#     print(f"Shortest word: {min(words, key=len)}")
#     print(f"Total characters: {sum(len(word) for word in words)}")
    
#     print_subsection_header("Type Checking and Conversion")
    
#     mixed = [1, 2.5, "3", 4, "5.5"]
#     print("Mixed list:", mixed)
    
#     # Filter by type
#     numbers_only = [x for x in mixed if isinstance(x, (int, float))]
#     strings_only = [x for x in mixed if isinstance(x, str)]
    
#     print("Numbers only:", numbers_only)
#     print("Strings only:", strings_only)
    
#     # Type conversion
#     try:
#         converted_numbers = [float(x) for x in mixed]
#         print("All converted to float:", converted_numbers)
#     except ValueError as e:
#         print(f"Conversion error: {e}")
    
#     print_subsection_header("All and Any Functions")
    
#     # all() - check if all elements are truthy
#     all_positive = [1, 2, 3, 4, 5]
#     has_zero = [1, 2, 0, 4, 5]
    
#     print(f"All positive numbers are truthy: {all(all_positive)}")
#     print(f"List with zero - all truthy: {all(has_zero)}")
    
#     # any() - check if any element is truthy
#     all_zeros = [0, 0, 0]
#     mixed_with_truth = [0, 0, 1, 0]
    
#     print(f"Any element in all zeros is truthy: {any(all_zeros)}")
#     print(f"Any element in mixed is truthy: {any(mixed_with_truth)}")

# # =============================================================================
# # 7. ADVANCED TECHNIQUES
# # =============================================================================

# def advanced_techniques():
#     """Demonstrate advanced list techniques."""
#     print_section_header("7. ADVANCED TECHNIQUES")
    
#     print_subsection_header("Tuple Unpacking with Lists")
    
#     # Unpacking coordinates
#     coordinates = [(10, 20), (30, 40), (50, 60)]
#     print("Coordinate pairs:", coordinates)
    
#     print("Unpacked coordinates:")
#     for x, y in coordinates:
#         print(f"  Point: ({x}, {y})")
    
#     # Unpacking with enumerate
#     colors = ["red", "green", "blue"]
#     print("Enumerate with unpacking:")
#     for index, color in enumerate(colors):
#         print(f"  Color {index + 1}: {color}")
    
#     print_subsection_header("List Wrapping Technique")
    
#     # Single category data
#     category_names = ["Fruits"]
#     category_items = ["apple", "banana", "orange"]
    
#     print("Category names:", category_names)
#     print("Category items:", category_items)
    
#     # Without list wrapping (problematic)
#     print("❌ Without list wrapping:")
#     for name, item in zip(category_names, category_items):
#         print(f"  {name}: {item}")  # Only pairs first elements
    
#     # With list wrapping (correct)
#     print("✅ With list wrapping:")
#     for name, items in zip(category_names, [category_items]):
#         print(f"  {name}: {', '.join(items)}")
    
#     print_subsection_header("Extended Unpacking with Asterisk")
    
#     # Unpacking with *
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
#     first, *middle, last = numbers
#     print(f"First: {first}")
#     print(f"Middle: {middle}")
#     print(f"Last: {last}")
    
#     # Head and tail
#     head, *tail = numbers
#     print(f"Head: {head}")
#     print(f"Tail: {tail}")
    
#     # Multiple assignments
#     *beginning, second_last, last = numbers
#     print(f"Beginning: {beginning}")
#     print(f"Second last: {second_last}")
#     print(f"Last: {last}")

# def list_manipulation_advanced():
#     """Demonstrate advanced list manipulation."""
#     print_subsection_header("Advanced List Manipulation")
    
#     # List rotation
#     original = [1, 2, 3, 4, 5]
#     print("Original list:", original)
    
#     # Rotate left by 2 positions
#     rotated_left = original[2:] + original[:2]
#     print("Rotated left by 2:", rotated_left)
    
#     # Rotate right by 2 positions  
#     rotated_right = original[-2:] + original[:-2]
#     print("Rotated right by 2:", rotated_right)
    
#     # Chunking a list
#     data = list(range(1, 21))  # [1, 2, 3, ..., 20]
#     chunk_size = 5
    
#     chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
#     print(f"Original data: {data}")
#     print(f"Chunks of {chunk_size}:")
#     for i, chunk in enumerate(chunks):
#         print(f"  Chunk {i + 1}: {chunk}")
    
#     # Remove duplicates while preserving order
#     with_duplicates = [1, 2, 3, 2, 4, 3, 5, 1, 6]
#     unique_ordered = []
#     seen = set()
#     for item in with_duplicates:
#         if item not in seen:
#             unique_ordered.append(item)
#             seen.add(item)
    
#     print("With duplicates:", with_duplicates)
#     print("Unique ordered:", unique_ordered)

# # =============================================================================
# # 8. NESTED LISTS
# # =============================================================================

# def nested_lists():
#     """Demonstrate working with nested lists."""
#     print_section_header("8. WORKING WITH NESTED LISTS")
    
#     print_subsection_header("Creating and Accessing Nested Lists")
    
#     # 2D matrix
#     matrix = [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ]
    
#     print("2D Matrix:")
#     for row in matrix:
#         print("  ", row)
    
#     # Accessing elements
#     print(f"Element at [1][2]: {matrix[1][2]}")  # 6
#     print(f"First row: {matrix[0]}")
#     print(f"Last column: [matrix[i][-1] for i in range(len(matrix))]: {[matrix[i][-1] for i in range(len(matrix))]}")
    
#     print_subsection_header("Nested List Operations")
    
#     # Modify nested list
#     matrix[1][1] = 99
#     print("After modifying [1][1] to 99:")
#     for row in matrix:
#         print("  ", row)
    
#     # Add row
#     matrix.append([10, 11, 12])
#     print("After adding new row:")
#     for row in matrix:
#         print("  ", row)
    
#     # Add column (more complex)
#     for row in matrix:
#         row.append(0)
#     print("After adding column of zeros:")
#     for row in matrix:
#         print("  ", row)
    
#     print_subsection_header("Flattening Nested Lists")
    
#     nested = [[1, 2], [3, 4, 5], [6], [7, 8, 9]]
#     print("Nested list:", nested)
    
#     # Method 1: List comprehension
#     flat1 = [item for sublist in nested for item in sublist]
#     print("Flattened (comprehension):", flat1)
    
#     # Method 2: Using sum with empty list
#     flat2 = sum(nested, [])
#     print("Flattened (sum trick):", flat2)
    
#     # Method 3: Using itertools.chain
#     import itertools
#     flat3 = list(itertools.chain.from_iterable(nested))
#     print("Flattened (itertools):", flat3)

# def matrix_operations():
#     """Demonstrate matrix operations with nested lists."""
#     print_subsection_header("Matrix Operations")
    
#     # Matrix addition
#     matrix_a = [[1, 2], [3, 4]]
#     matrix_b = [[5, 6], [7, 8]]
    
#     print("Matrix A:")
#     for row in matrix_a:
#         print("  ", row)
    
#     print("Matrix B:")
#     for row in matrix_b:
#         print("  ", row)
    
#     # Element-wise addition
#     result = [[matrix_a[i][j] + matrix_b[i][j] 
#               for j in range(len(matrix_a[0]))] 
#               for i in range(len(matrix_a))]
    
#     print("A + B:")
#     for row in result:
#         print("  ", row)
    
#     # Matrix transpose
#     matrix = [[1, 2, 3], [4, 5, 6]]
#     transposed = [[matrix[j][i] for j in range(len(matrix))] 
#                   for i in range(len(matrix[0]))]
    
#     print("Original matrix:")
#     for row in matrix:
#         print("  ", row)
    
#     print("Transposed:")
#     for row in transposed:
#         print("  ", row)

# # =============================================================================
# # 9. PERFORMANCE TIPS
# # =============================================================================

# def performance_tips():
#     """Demonstrate performance considerations for lists."""
#     print_section_header("9. PERFORMANCE TIPS")
    
#     print_subsection_header("Efficient List Building")
    
#     # ❌ Inefficient: Concatenation in loop
#     print("❌ Inefficient concatenation:")
#     result = []
#     for i in range(5):
#         result = result + [i]  # Creates new list each time
#     print("Result:", result)
    
#     # ✅ Efficient: append() method
#     print("✅ Efficient append:")
#     result = []
#     for i in range(5):
#         result.append(i)  # Modifies existing list
#     print("Result:", result)
    
#     # ✅ Most efficient: List comprehension
#     print("✅ Most efficient - list comprehension:")
#     result = [i for i in range(5)]
#     print("Result:", result)
    
#     print_subsection_header("Memory Considerations")
    
#     # Large lists - be mindful of memory
#     large_list = list(range(1000000))
#     print(f"Large list length: {len(large_list)}")
#     print(f"Memory tip: Use generators for large datasets when possible")
    
#     # Generator vs List
#     def show_memory_difference():
#         import sys
        
#         # List (stores all values in memory)
#         list_comp = [x for x in range(1000)]
#         list_size = sys.getsizeof(list_comp)
        
#         # Generator (stores only the logic)
#         gen_comp = (x for x in range(1000))
#         gen_size = sys.getsizeof(gen_comp)
        
#         print(f"List comprehension size: {list_size} bytes")
#         print(f"Generator expression size: {gen_size} bytes")
#         print(f"Memory saved: {list_size - gen_size} bytes")
    
#     show_memory_difference()
    
#     print_subsection_header("Search Performance")
    
#     # Linear search vs set lookup
#     large_list = list(range(10000))
#     search_set = set(large_list)
    
#     target = 9999
    
#     print(f"Searching for {target}:")
#     print(f"In list (linear search): {'Found' if target in large_list else 'Not found'}")
#     print(f"In set (hash lookup): {'Found' if target in search_set else 'Not found'}")
#     print("💡 Tip: Use sets for frequent membership testing")
    
#     print_subsection_header("Best Practices Summary")
    
#     best_practices = [
#         "Use list comprehensions for simple transformations",
#         "Use append() instead of concatenation in loops",
#         "Consider generators for large datasets",
#         "Use sets for frequent membership testing",
#         "Preallocate list size if known: [None] * size",
#         "Use extend() to add multiple items efficiently",
#         "Use slicing for bulk operations when possible"
#     ]
    
#     print("🚀 Performance Best Practices:")
#     for i, practice in enumerate(best_practices, 1):
#         print(f"  {i}. {practice}")

# # =============================================================================
# # 10. REAL-WORLD EXAMPLES
# # =============================================================================

# def real_world_examples():
#     """Demonstrate practical real-world applications."""
#     print_section_header("10. REAL-WORLD EXAMPLES")
    
#     print_subsection_header("Example 1: Student Grade Management")
    
#     # Student data management
#     students = [
#         {"name": "Alice", "grades": [95, 87, 92, 88]},
#         {"name": "Bob", "grades": [78, 85, 80, 83]},
#         {"name": "Charlie", "grades": [92, 88, 95, 90]},
#         {"name": "Diana", "grades": [87, 91, 89, 94]}
#     ]
    
#     print("Student Grade Analysis:")
#     print("-" * 40)
    
#     for student in students:
#         name = student["name"]
#         grades = student["grades"]
#         average = sum(grades) / len(grades)
#         highest = max(grades)
#         lowest = min(grades)
        
#         print(f"{name}:")
#         print(f"  Grades: {grades}")
#         print(f"  Average: {average:.2f}")
#         print(f"  Highest: {highest}")
#         print(f"  Lowest: {lowest}")
#         print(f"  Status: {'Honor Roll' if average >= 90 else 'Good Standing' if average >= 80 else 'Needs Improvement'}")
#         print()
    
#     # Class statistics
#     all_grades = [grade for student in students for grade in student["grades"]]
#     class_average = sum(all_grades) / len(all_grades)
#     print(f"Class Statistics:")
#     print(f"  Total students: {len(students)}")
#     print(f"  Class average: {class_average:.2f}")
#     print(f"  Highest grade: {max(all_grades)}")
#     print(f"  Lowest grade: {min(all_grades)}")
    
#     print_subsection_header("Example 2: Shopping Cart System")
    
#     # Shopping cart with inventory management
#     inventory = {
#         "laptop": {"price": 999.99, "stock": 5},
#         "mouse": {"price": 29.99, "stock": 20},
#         "keyboard": {"price": 79.99, "stock": 15},
#         "monitor": {"price": 299.99, "stock": 8}
#     }
    
#     cart = [
#         {"item": "laptop", "quantity": 1},
#         {"item": "mouse", "quantity": 2},
#         {"item": "keyboard", "quantity": 1}
#     ]
    
#     print("Shopping Cart Analysis:")
#     print("-" * 30)
    
#     total_cost = 0
#     valid_cart = True
    
#     for cart_item in cart:
#         item_name = cart_item["item"]
#         quantity = cart_item["quantity"]
        
#         if item_name in inventory:
#             item_info = inventory[item_name]
#             price = item_info["price"]
#             stock = item_info["stock"]
            
#             if quantity <= stock:
#                 item_total = price * quantity
#                 total_cost += item_total
#                 print(f"{item_name.title()}: {quantity} x ${price:.2f} = ${item_total:.2f}")
#             else:
#                 print(f"❌ {item_name.title()}: Not enough stock! (Requested: {quantity}, Available: {stock})")
#                 valid_cart = False
#         else:
#             print(f"❌ {item_name.title()}: Item not found!")
#             valid_cart = False
    
#     print("-" * 30)
#     if valid_cart:
#         tax = total_cost * 0.08  # 8% tax
#         final_total = total_cost + tax
#         print(f"Subtotal: ${total_cost:.2f}")
#         print(f"Tax (8%): ${tax:.2f}")
#         print(f"Total: ${final_total:.2f}")
#     else:
#         print("❌ Cart contains invalid items. Please review.")
    
#     print_subsection_header("Example 3: Data Processing Pipeline")
    
#     # Simulating data processing
#     raw_data = [
#         "  alice@email.com  ",
#         "BOB@EMAIL.COM",
#         "",
#         "charlie@email.com",
#         "invalid-email",
#         "diana@email.com  ",
#         None,
#         "eve@email.com"
#     ]
    
#     print("Data Processing Pipeline:")
#     print(f"Raw data: {raw_data}")
    
#     # Step 1: Remove None and empty values
#     step1 = [item for item in raw_data if item is not None and str(item).strip()]
#     print(f"After removing None/empty: {step1}")
    
#     # Step 2: Clean whitespace and convert to lowercase
#     step2 = [item.strip().lower() for item in step1]
#     print(f"After cleaning: {step2}")
    
#     # Step 3: Validate email format (simple check)
#     step3 = [email for email in step2 if "@" in email and "." in email.split("@")[1]]
#     print(f"After validation: {step3}")
    
#     # Step 4: Remove duplicates while preserving order
#     step4 = []
#     seen = set()
#     for email in step3:
#         if email not in seen:
#             step4.append(email)
#             seen.add(email)
    
#     print(f"Final processed data: {step4}")
#     print(f"Processing summary: {len(raw_data)} → {len(step4)} valid emails")

# def todo_list_example():
#     """Demonstrate a todo list application."""
#     print_subsection_header("Example 4: Todo List Manager")
    
#     class TodoList:
#         def __init__(self):
#             self.tasks = []
        
#         def add_task(self, task, priority="medium"):
#             self.tasks.append({
#                 "task": task,
#                 "priority": priority,
#                 "completed": False,
#                 "id": len(self.tasks) + 1
#             })
#             print(f"✅ Added: {task}")
        
#         def complete_task(self, task_id):
#             for task in self.tasks:
#                 if task["id"] == task_id:
#                     task["completed"] = True
#                     print(f"✅ Completed: {task['task']}")
#                     return
#             print(f"❌ Task {task_id} not found")
        
#         def list_tasks(self, show_completed=True):
#             if not self.tasks:
#                 print("No tasks found!")
#                 return
            
#             print("\n📋 Current Tasks:")
#             print("-" * 50)
            
#             for task in self.tasks:
#                 if not show_completed and task["completed"]:
#                     continue
                
#                 status = "✓" if task["completed"] else "○"
#                 priority_icon = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(task["priority"], "⚪")
                
#                 print(f"{status} [{task['id']}] {priority_icon} {task['task']}")
        
#         def get_summary(self):
#             total = len(self.tasks)
#             completed = len([t for t in self.tasks if t["completed"]])
#             pending = total - completed
            
#             return {
#                 "total": total,
#                 "completed": completed,
#                 "pending": pending
#             }
    
#     # Demo the todo list
#     todo = TodoList()
    
#     # Add some tasks
#     todo.add_task("Complete Python list guide", "high")
#     todo.add_task("Review code examples", "medium")
#     todo.add_task("Write documentation", "medium")
#     todo.add_task("Test edge cases", "low")
    
#     # Show all tasks
#     todo.list_tasks()
    
#     # Complete some tasks
#     todo.complete_task(1)
#     todo.complete_task(3)
    
#     # Show updated list
#     print("\n📊 Updated Task List:")
#     todo.list_tasks()
    
#     # Show summary
#     summary = todo.get_summary()
#     print(f"\n📈 Summary: {summary['completed']}/{summary['total']} completed, {summary['pending']} pending")

# # =============================================================================
# # 11. INTERACTIVE DEMONSTRATIONS
# # =============================================================================

# def interactive_demonstrations():
#     """Provide interactive examples for hands-on learning."""
#     print_section_header("11. INTERACTIVE DEMONSTRATIONS")
    
#     print_subsection_header("Demo 1: List Builder")
    
#     def list_builder_demo():
#         print("🛠️ Interactive List Builder")
#         print("Build a list step by step and see the results!")
        
#         my_list = []
        
#         operations = [
#             ("Add 'apple'", lambda: my_list.append('apple')),
#             ("Add 'banana'", lambda: my_list.append('banana')),
#             ("Insert 'orange' at index 1", lambda: my_list.insert(1, 'orange')),
#             ("Extend with ['grape', 'kiwi']", lambda: my_list.extend(['grape', 'kiwi'])),
#             ("Remove 'banana'", lambda: my_list.remove('banana')),
#             ("Pop last element", lambda: my_list.pop()),
#             ("Sort the list", lambda: my_list.sort()),
#             ("Reverse the list", lambda: my_list.reverse())
#         ]
        
#         for description, operation in operations:
#             print(f"\n{description}")
#             operation()
#             print(f"Result: {my_list}")
    
#     list_builder_demo()
    
#     print_subsection_header("Demo 2: List Comprehension Workshop")
    
#     def comprehension_workshop():
#         print("🎯 List Comprehension Workshop")
        
#         numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#         print(f"Starting with: {numbers}")
        
#         examples = [
#             ("Squares", [x**2 for x in numbers]),
#             ("Even numbers only", [x for x in numbers if x % 2 == 0]),
#             ("Odd squares", [x**2 for x in numbers if x % 2 == 1]),
#             ("Numbers > 5, doubled", [x*2 for x in numbers if x > 5]),
#             ("Even/Odd labels", ["even" if x % 2 == 0 else "odd" for x in numbers[:5]])
#         ]
        
#         for description, result in examples:
#             print(f"\n{description}: {result}")
    
#     comprehension_workshop()
    
#     print_subsection_header("Demo 3: Data Transformation Pipeline")
    
#     def transformation_pipeline():
#         print("🔄 Data Transformation Pipeline")
        
#         # Sample messy data
#         messy_data = [
#             "  John Doe, 25, Engineer  ",
#             "jane smith,30,designer",
#             "BOB JOHNSON, 35, MANAGER",
#             "",
#             "alice brown,28,developer",
#             None,
#             "charlie davis,32,analyst"
#         ]
        
#         print("Original messy data:")
#         for i, item in enumerate(messy_data):
#             print(f"  {i}: {repr(item)}")
        
#         # Transformation steps
#         print("\n🔧 Transformation steps:")
        
#         # Step 1: Filter out None and empty
#         step1 = [item for item in messy_data if item and str(item).strip()]
#         print(f"1. Remove None/empty: {len(step1)} items")
        
#         # Step 2: Clean and split
#         step2 = [item.strip().split(',') for item in step1]
#         print(f"2. Split by comma: {step2}")
        
#         # Step 3: Clean each field and create structured data
#         step3 = []
#         for person_data in step2:
#             if len(person_data) == 3:
#                 name = person_data[0].strip().title()
#                 age = int(person_data[1].strip())
#                 job = person_data[2].strip().title()
#                 step3.append({"name": name, "age": age, "job": job})
        
#         print("3. Create structured data:")
#         for person in step3:
#             print(f"   {person}")
        
#         # Step 4: Analysis
#         print("\n📊 Analysis:")
#         average_age = sum(person["age"] for person in step3) / len(step3)
#         print(f"   Average age: {average_age:.1f}")
#         print(f"   Youngest: {min(step3, key=lambda p: p['age'])['name']}")
#         print(f"   Oldest: {max(step3, key=lambda p: p['age'])['name']}")
        
#         # Job distribution
#         jobs = [person["job"] for person in step3]
#         job_counts = {job: jobs.count(job) for job in set(jobs)}
#         print(f"   Job distribution: {job_counts}")
    
#     transformation_pipeline()

# # =============================================================================
# # 12. QUICK REFERENCE
# # =============================================================================

# def quick_reference():
#     """Provide a comprehensive quick reference guide."""
#     print_section_header("12. QUICK REFERENCE GUIDE")
    
#     reference_sections = {
#         "🔨 List Creation": [
#             "[]                          # Empty list",
#             "[1, 2, 3]                  # With elements",
#             "list(range(5))             # From range: [0, 1, 2, 3, 4]",
#             "list('hello')              # From string: ['h', 'e', 'l', 'l', 'o']",
#             "[0] * 5                    # Repeated elements: [0, 0, 0, 0, 0]"
#         ],
        
#         "📍 Accessing Elements": [
#             "lst[0]                     # First element",
#             "lst[-1]                    # Last element",
#             "lst[1:3]                   # Slice [1, 2]",
#             "lst[:3]                    # First 3 elements",
#             "lst[::2]                   # Every 2nd element",
#             "lst[::-1]                  # Reverse list"
#         ],
        
#         "➕ Adding Elements": [
#             "lst.append(item)           # Add to end",
#             "lst.insert(i, item)        # Insert at index",
#             "lst.extend(other)          # Add all from other",
#             "lst += other               # Concatenate",
#             "lst = lst + other          # Create new list"
#         ],
        
#         "➖ Removing Elements": [
#             "lst.remove(item)           # Remove first occurrence",
#             "lst.pop()                  # Remove and return last",
#             "lst.pop(i)                 # Remove and return at index",
#             "del lst[i]                 # Delete at index",
#             "lst.clear()                # Remove all"
#         ],
        
#         "🔍 Searching & Counting": [
#             "item in lst                # Check membership",
#             "lst.index(item)            # Find index",
#             "lst.count(item)            # Count occurrences",
#             "lst.index(item, start)     # Find from start index"
#         ],
        
#         "🔄 Sorting & Reversing": [
#             "lst.sort()                 # Sort in place",
#             "lst.sort(reverse=True)     # Sort descending",
#             "sorted(lst)                # Return sorted copy",
#             "lst.reverse()              # Reverse in place",
#             "lst[::-1]                  # Return reversed copy"
#         ],
        
#         "📊 Built-in Functions": [
#             "len(lst)                   # Length",
#             "max(lst)                   # Maximum value",
#             "min(lst)                   # Minimum value",
#             "sum(lst)                   # Sum of numbers",
#             "all(lst)                   # All truthy?",
#             "any(lst)                   # Any truthy?"
#         ],
        
#         "🔁 Iteration": [
#             "for item in lst:           # Simple iteration",
#             "for i, item in enumerate(lst):  # With index",
#             "for a, b in zip(lst1, lst2):    # Multiple lists",
#             "for i in range(len(lst)):       # Index-based"
#         ],
        
#         "🎯 List Comprehensions": [
#             "[x for x in lst]           # Copy list",
#             "[x*2 for x in lst]         # Transform",
#             "[x for x in lst if x > 0]  # Filter",
#             "[f(x) for x in lst if cond(x)]  # Transform + filter"
#         ],
        
#         "🧮 Common Patterns": [
#             "lst1 + lst2                # Concatenate",
#             "lst * 3                    # Repeat 3 times",
#             "lst.copy()                 # Shallow copy",
#             "lst[:]                     # Also shallow copy",
#             "list(lst)                  # Convert to list"
#         ]
#     }
    
#     for section_title, items in reference_sections.items():
#         print_subsection_header(section_title)
#         for item in items:
#             print(f"  {item}")
#         print()

# def common_pitfalls():
#     """Show common pitfalls and how to avoid them."""
#     print_subsection_header("⚠️ Common Pitfalls")
    
#     pitfalls = [
#         {
#             "title": "Mutable Default Arguments",
#             "wrong": "def add_item(item, lst=[]):  # DON'T DO THIS",
#             "right": "def add_item(item, lst=None):\n    if lst is None:\n        lst = []",
#             "explanation": "Default mutable arguments are shared between function calls"
#         },
#         {
#             "title": "List Multiplication with Mutable Objects",
#             "wrong": "matrix = [[0] * 3] * 3  # All rows reference same list!",
#             "right": "matrix = [[0] * 3 for _ in range(3)]",
#             "explanation": "Multiplication creates references, not copies"
#         },
#         {
#             "title": "Modifying List While Iterating",
#             "wrong": "for item in lst:\n    if condition:\n        lst.remove(item)  # Can skip elements",
#             "right": "lst = [item for item in lst if not condition]",
#             "explanation": "Removing items changes indices during iteration"
#         },
#         {
#             "title": "Confusing append() vs extend()",
#             "wrong": "lst.append([1, 2, 3])  # Adds the list as single item",
#             "right": "lst.extend([1, 2, 3])  # Adds each item individually",
#             "explanation": "append() adds one item, extend() adds multiple items"
#         }
#     ]
    
#     for i, pitfall in enumerate(pitfalls, 1):
#         print(f"{i}. {pitfall['title']}")
#         print(f"   ❌ Wrong: {pitfall['wrong']}")
#         print(f"   ✅ Right: {pitfall['right']}")
#         print(f"   💡 Why: {pitfall['explanation']}")
#         print()

# =============================================================================
# MAIN EXECUTION AND MENU SYSTEM
# =============================================================================

def show_menu():
    """Display the main menu."""
    menu_items = [
        ("1", "List Basics", list_basics),
        ("2", "Basic Operations", basic_operations),
        ("3", "List Methods", list_methods),
        ("4", "List Comprehensions", list_comprehensions),
        ("5", "Iteration Techniques", iteration_techniques),
        ("6", "List Functions", list_functions),
        ("7", "Advanced Techniques", advanced_techniques),
        ("8", "Nested Lists", nested_lists),
        ("9", "Performance Tips", performance_tips),
        ("10", "Real-World Examples", real_world_examples),
        ("11", "Interactive Demos", interactive_demonstrations),
        ("12", "Quick Reference", quick_reference),
        ("A", "All Sections", run_all_sections),
        ("T", "Table of Contents", show_table_of_contents),
        ("Q", "Quit", None)
    ]
    
    print("\n" + "=" * 60)
    print(" PYTHON LISTS GUIDE - MAIN MENU ".center(60, "="))
    print("=" * 60)
    
    for key, title, _ in menu_items:
        print(f"  {key}. {title}")
    
    print("=" * 60)
    return menu_items

def run_all_sections():
    """Run all sections in sequence."""
    sections = [
        ("List Basics", list_basics),
        ("List Slicing", list_slicing_demo),
        ("Basic Operations", basic_operations),
        ("List Methods", list_methods),
        ("List Comprehensions", list_comprehensions),
        ("Nested List Comprehensions", nested_list_comprehensions),
        ("Iteration Techniques", iteration_techniques),
        ("Range and Indices", range_and_indices),
        ("List Functions", list_functions),
        ("Advanced Techniques", advanced_techniques),
        ("Advanced List Manipulation", list_manipulation_advanced),
        ("Nested Lists", nested_lists),
        ("Matrix Operations", matrix_operations),
        ("Performance Tips", performance_tips),
        ("Real-World Examples", real_world_examples),
        ("Todo List Example", todo_list_example),
        ("Interactive Demonstrations", interactive_demonstrations),
        ("Quick Reference", quick_reference),
        ("Common Pitfalls", common_pitfalls)
    ]
    
    print_section_header("RUNNING ALL SECTIONS")
    print("🚀 This will run through all sections of the guide.")
    print("📖 Each section includes examples and demonstrations.")
    print("⏸️  You can pause between sections to review the content.")
    
    for i, (title, func) in enumerate(sections, 1):
        print(f"\n🔹 Running Section {i}/{len(sections)}: {title}")
        run_example(func)
        
        if i < len(sections):  # Don't pause after the last section
            pause_for_user()

def main():
    """Main function to run the guide."""
    print("🐍 Welcome to the Complete Python Lists Guide!")
    print("This interactive guide will teach you everything about Python lists.")
    
    # Show table of contents first
    show_table_of_contents()
    
    while True:
        menu_items = show_menu()
        choice = input("\n📝 Enter your choice: ").strip().upper()
        
        # Find the selected menu item
        selected_item = None
        for key, title, func in menu_items:
            if key.upper() == choice:
                selected_item = (key, title, func)
                break
        
        if not selected_item:
            print("❌ Invalid choice. Please try again.")
            continue
        
        key, title, func = selected_item
        
        if key.upper() == "Q":
            print("\n👋 Thank you for using the Python Lists Guide!")
            print("🎯 Happy coding with Python lists!")
            break
        
        if func:
            print(f"\n🚀 Running: {title}")
            run_example(func)
            
            # Ask if user wants to continue
            continue_choice = input("\n🔄 Press Enter to return to menu (or 'q' to quit): ").strip().lower()
            if continue_choice == 'q':
                print("\n👋 Thank you for using the Python Lists Guide!")
                break

if __name__ == "__main__":
    main()