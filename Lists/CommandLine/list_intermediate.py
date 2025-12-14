from utility import print_section_header, print_subsection_header, run_example, pause_for_user


# =============================================================================
# LIST METHODS
# =============================================================================

def list_methods():
    """Demonstrate essential list methods."""
    print_section_header("3. LIST METHODS")
    
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print("Working with:", numbers)
    
    print_subsection_header("Searching and Counting")
    
    # count() - count occurrences
    print("Count of 1:", numbers.count(1))
    print("Count of 5:", numbers.count(5))
    
    # index() - find first occurrence
    print("Index of 4:", numbers.index(4))
    print("Index of 5:", numbers.index(5))  # First occurrence
    
    print_subsection_header("Sorting and Reversing")
    
    # sort() - sort in place
    numbers_copy = numbers.copy()
    numbers_copy.sort()
    print("Sorted (ascending):", numbers_copy)
    
    numbers_copy.sort(reverse=True)
    print("Sorted (descending):", numbers_copy)
    
    # sorted() - return new sorted list
    original = [3, 1, 4, 1, 5]
    sorted_list = sorted(original)
    print("Original:", original)
    print("Sorted copy:", sorted_list)
    
    # reverse() - reverse in place
    letters = ['a', 'b', 'c', 'd']
    print("Original letters:", letters)
    letters.reverse()
    print("After reverse():", letters)
    
    print_subsection_header("Copying Lists")
    
    # copy() - shallow copy
    original = [1, 2, [3, 4]]
    shallow = original.copy()
    deep_copy = [item[:] if isinstance(item, list) else item for item in original]
    
    print("Original:", original)
    print("Shallow copy:", shallow)
    
    # Demonstrate shallow vs deep copy
    original[2].append(5)
    print("After modifying nested list in original:")
    print("Original:", original)
    print("Shallow copy (affected):", shallow)

# =============================================================================
# LIST COMPREHENSIONS
# =============================================================================

def list_comprehensions():
    """Demonstrate list comprehensions."""
    print_section_header("4. LIST COMPREHENSIONS")
    
    print_subsection_header("Basic List Comprehensions")
    
    # Basic syntax: [expression for item in iterable]
    squares = [x**2 for x in range(1, 6)]
    print("Squares of 1-5:", squares)
    
    # String manipulation
    words = ["hello", "world", "python"]
    uppercase = [word.upper() for word in words]
    print("Uppercase words:", uppercase)
    
    # Working with existing list
    numbers = [1, 2, 3, 4, 5]
    doubled = [n * 2 for n in numbers]
    print("Doubled numbers:", doubled)
    
    print_subsection_header("Conditional List Comprehensions")
    
    # With if condition
    even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
    print("Even squares 1-10:", even_squares)
    
    # Conditional expression
    signs = ["positive" if x > 0 else "negative" if x < 0 else "zero" 
             for x in [-2, -1, 0, 1, 2]]
    print("Number signs:", signs)
    
    print_subsection_header("Working with Strings")
    
    sentence = "Hello World Python Programming"
    # Extract words longer than 5 characters
    long_words = [word for word in sentence.split() if len(word) > 5]
    print("Words longer than 5 chars:", long_words)
    
    # Extract vowels from a string
    text = "Python Programming"
    vowels = [char for char in text.lower() if char in 'aeiou']
    print("Vowels in text:", vowels)
    
    print_subsection_header("Working with Dictionaries")
    
    # From dictionary to list
    student_grades = {"Alice": 95, "Bob": 87, "Charlie": 92, "Diana": 98}
    
    # List of names
    names = [name for name in student_grades.keys()]
    print("Student names:", names)
    
    # List of high grades
    high_grades = [grade for grade in student_grades.values() if grade >= 90]
    print("Grades >= 90:", high_grades)
    
    # List of tuples
    name_grade_pairs = [(name, grade) for name, grade in student_grades.items()]
    print("Name-grade pairs:", name_grade_pairs)
    
    # List of dictionaries with conditions
    high_performers = [{"name": name, "grade": grade} 
                      for name, grade in student_grades.items() 
                      if grade >= 90]
    print("High performers:", high_performers)

def nested_list_comprehensions():
    """Demonstrate nested list comprehensions."""
    print_subsection_header("Nested List Comprehensions")
    
    # Create a multiplication table
    multiplication_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
    print("5x5 Multiplication table:")
    for row in multiplication_table:
        print(row)
    
    # Flatten a nested list
    nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [item for sublist in nested for item in sublist]
    print("Original nested:", nested)
    print("Flattened:", flattened)
    
    # Matrix transpose
    matrix = [[1, 2, 3], [4, 5, 6]]
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    print("Original matrix:", matrix)
    print("Transposed:", transposed)

# =============================================================================
# ITERATION TECHNIQUES
# =============================================================================

def iteration_techniques():
    """Demonstrate various ways to iterate over lists."""
    print_section_header("5. ITERATION TECHNIQUES")
    
    fruits = ["apple", "banana", "cherry", "date"]
    prices = [1.20, 0.50, 2.30, 3.00]
    
    print_subsection_header("Basic Iteration")
    
    # Simple for loop
    print("Simple iteration:")
    for fruit in fruits:
        print(f"  - {fruit}")
    
    print_subsection_header("Enumerate - Index and Value")
    
    # enumerate() for index and value
    print("With enumerate (index, value):")
    for index, fruit in enumerate(fruits):
        print(f"  {index}: {fruit}")
    
    # enumerate with custom start
    print("Enumerate with start=1:")
    for index, fruit in enumerate(fruits, start=1):
        print(f"  {index}. {fruit}")
    
    print_subsection_header("Zip - Multiple Lists")
    
    # zip() to iterate over multiple lists
    print("Zip fruits and prices:")
    for fruit, price in zip(fruits, prices):
        print(f"  {fruit}: ${price:.2f}")
    
    # zip with unequal lengths
    colors = ["red", "yellow", "red"]  # shorter list
    print("Zip with unequal lengths:")
    for fruit, price, color in zip(fruits, prices, colors):
        print(f"  {fruit} (${price:.2f}) - {color}")
    
    print_subsection_header("Advanced Iteration")
    
    # Iteration with conditions
    print("Expensive fruits (> $2.00):")
    for fruit, price in zip(fruits, prices):
        if price > 2.00:
            print(f"  {fruit}: ${price:.2f}")
    
    # Iteration with enumerate and zip
    print("Detailed fruit information:")
    for index, (fruit, price) in enumerate(zip(fruits, prices), 1):
        status = "Expensive" if price > 2.00 else "Affordable"
        print(f"  {index}. {fruit}: ${price:.2f} ({status})")

def range_and_indices():
    """Demonstrate iteration using range and indices."""
    print_subsection_header("Using Range and Indices")
    
    numbers = [10, 20, 30, 40, 50]
    
    # Traditional index-based iteration
    print("Index-based iteration:")
    for i in range(len(numbers)):
        print(f"  Index {i}: {numbers[i]}")
    
    # Reverse iteration using indices
    print("Reverse iteration with indices:")
    for i in range(len(numbers) - 1, -1, -1):
        print(f"  Index {i}: {numbers[i]}")
    
    # Step iteration
    print("Every second element:")
    for i in range(0, len(numbers), 2):
        print(f"  Index {i}: {numbers[i]}")

