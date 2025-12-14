"""
COMPLETE GUIDE TO PYTHON SETS
=============================

A comprehensive guide to working with Python sets, covering everything from basic operations
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
        print(f"Error running example: {e}")

def pause_for_user():
    """Pause execution for user to review output."""
    input("\nPress Enter to continue to the next section...")

# =============================================================================
# TABLE OF CONTENTS
# =============================================================================

def show_table_of_contents():
    """Display the guide's table of contents."""
    print_section_header("PYTHON SETS - COMPLETE GUIDE", "=")
    
    toc = """
TABLE OF CONTENTS:

1. Set Basics - Creation, Access, and Properties
2. Set Operations - Union, Intersection, Difference, and More
3. Set Methods - Essential built-in methods
4. Set Comprehensions - Efficient set creation
5. Set Iteration Techniques - Various ways to loop through sets
6. Set vs List vs Tuple Comparison - Performance and usage
7. Advanced Set Techniques - Sorting, filtering, and optimization
8. Frozen Sets - Immutable sets
9. Practical Applications - Real-world use cases
10. Set Performance Analysis - Memory and speed considerations

SPECIAL FEATURES:
- Interactive examples for each concept
- Performance comparisons
- Memory usage analysis
- Best practices and common pitfalls
- Real-world applications

Press the corresponding number to explore each section.
    """
    print(toc)

# =============================================================================
# 1. SET BASICS
# =============================================================================

def set_creation_examples():
    """Demonstrate different ways to create sets."""
    print_section_header("1. SET CREATION AND BASICS")
    
    print("Sets are unordered collections of unique elements.")
    print("Let's explore different ways to create sets:\n")
    
    # Empty set creation
    print("1. Creating an empty set:")
    empty_set = set()
    print(f"   empty_set = set()  # {empty_set}")
    print(f"   Type: {type(empty_set)}")
    print("   Note: {} creates an empty dict, not set!")
    
    # Set from literals
    print("\n2. Creating sets from literals:")
    fruits = {"apple", "banana", "cherry", "apple"}  # Note: duplicate 'apple'
    print(f"   fruits = {{'apple', 'banana', 'cherry', 'apple'}}")
    print(f"   Result: {fruits}  # Duplicates automatically removed!")
    
    # Set from lists
    print("\n3. Creating sets from other iterables:")
    numbers_list = [1, 2, 3, 3, 4, 4, 5]
    numbers_set = set(numbers_list)
    print(f"   numbers_list = {numbers_list}")
    print(f"   numbers_set = set(numbers_list)")
    print(f"   Result: {numbers_set}")
    
    # Set from string
    string_set = set("hello")
    print(f"\n   set('hello') = {string_set}")
    
    # Mixed data types
    print("\n4. Sets with mixed data types:")
    mixed_set = {1, "hello", 3.14, True}
    print(f"   mixed_set = {mixed_set}")
    print("   Note: True and 1 are considered equal in sets!")
    
    # Hashable elements only
    print("\n5. Set elements must be hashable:")
    try:
        # This will cause an error
        invalid_set = {[1, 2, 3]}
    except TypeError as e:
        print(f"   {{[1, 2, 3]}} causes error: {e}")
    
    print(f"\n   Valid hashable types: int, float, str, tuple, frozenset")
    hashable_set = {1, 3.14, "text", (1, 2), frozenset([3, 4])}
    print(f"   Example: {hashable_set}")

def set_properties_examples():
    """Demonstrate key properties of sets."""
    print_subsection_header("Set Properties and Characteristics")
    
    sample_set = {3, 1, 4, 1, 5, 9, 2, 6}
    print(f"Sample set: {sample_set}")
    
    print("\n1. Unordered collection:")
    print("   Sets don't maintain insertion order (before Python 3.7)")
    print("   From Python 3.7+, sets preserve insertion order")
    
    print("\n2. Unique elements only:")
    duplicates = [1, 1, 2, 2, 3, 3]
    unique_set = set(duplicates)
    print(f"   Original list: {duplicates}")
    print(f"   Set result: {unique_set}")
    
    print("\n3. Mutable (can be modified):")
    mutable_set = {1, 2, 3}
    print(f"   Original: {mutable_set}")
    mutable_set.add(4)
    print(f"   After add(4): {mutable_set}")
    mutable_set.remove(1)
    print(f"   After remove(1): {mutable_set}")
    
    print("\n4. Not indexed (no indexing like lists):")
    print("   sets[0] would cause TypeError!")
    print("   Use 'in' operator for membership testing instead")
    
    print(f"\n5. Length and membership:")
    print(f"   len(sample_set) = {len(sample_set)}")
    print(f"   4 in sample_set = {4 in sample_set}")
    print(f"   10 in sample_set = {10 in sample_set}")

# =============================================================================
# 2. SET OPERATIONS
# =============================================================================

def set_operations_examples():
    """Demonstrate mathematical set operations."""
    print_section_header("2. SET OPERATIONS")
    
    # Sample sets for demonstrations
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    set_c = {1, 3, 5, 7, 9}
    
    print(f"Sample sets:")
    print(f"set_a = {set_a}")
    print(f"set_b = {set_b}")
    print(f"set_c = {set_c}")
    
    print_subsection_header("Union Operations")
    print("Union combines all unique elements from sets")
    
    # Union using | operator
    union_op = set_a | set_b
    print(f"set_a | set_b = {union_op}")
    
    # Union using union() method
    union_method = set_a.union(set_b)
    print(f"set_a.union(set_b) = {union_method}")
    
    # Multiple set union
    union_multiple = set_a | set_b | set_c
    print(f"set_a | set_b | set_c = {union_multiple}")
    
    print_subsection_header("Intersection Operations")
    print("Intersection finds common elements")
    
    # Intersection using & operator
    intersection_op = set_a & set_b
    print(f"set_a & set_b = {intersection_op}")
    
    # Intersection using intersection() method
    intersection_method = set_a.intersection(set_b)
    print(f"set_a.intersection(set_b) = {intersection_method}")
    
    # Multiple set intersection
    intersection_multiple = set_a & set_b & set_c
    print(f"set_a & set_b & set_c = {intersection_multiple}")
    
    print_subsection_header("Difference Operations")
    print("Difference finds elements in first set but not in second")
    
    # Difference using - operator
    difference_op = set_a - set_b
    print(f"set_a - set_b = {difference_op}")
    
    # Difference using difference() method
    difference_method = set_a.difference(set_b)
    print(f"set_a.difference(set_b) = {difference_method}")
    
    # Reverse difference
    reverse_diff = set_b - set_a
    print(f"set_b - set_a = {reverse_diff}")
    
    print_subsection_header("Symmetric Difference Operations")
    print("Symmetric difference finds elements in either set, but not both")
    
    # Symmetric difference using ^ operator
    sym_diff_op = set_a ^ set_b
    print(f"set_a ^ set_b = {sym_diff_op}")
    
    # Symmetric difference using symmetric_difference() method
    sym_diff_method = set_a.symmetric_difference(set_b)
    print(f"set_a.symmetric_difference(set_b) = {sym_diff_method}")

def set_comparison_examples():
    """Demonstrate set comparison operations."""
    print_subsection_header("Set Comparison Operations")
    
    set1 = {1, 2, 3}
    set2 = {1, 2, 3, 4, 5}
    set3 = {3, 4, 5}
    set4 = {1, 2, 3}
    
    print(f"set1 = {set1}")
    print(f"set2 = {set2}")
    print(f"set3 = {set3}")
    print(f"set4 = {set4}")
    
    print("\n1. Equality:")
    print(f"   set1 == set4: {set1 == set4}")
    print(f"   set1 == set2: {set1 == set2}")
    
    print("\n2. Subset operations:")
    print(f"   set1.issubset(set2): {set1.issubset(set2)}")
    print(f"   set1 <= set2: {set1 <= set2}")
    print(f"   set1 < set2 (proper subset): {set1 < set2}")
    
    print("\n3. Superset operations:")
    print(f"   set2.issuperset(set1): {set2.issuperset(set1)}")
    print(f"   set2 >= set1: {set2 >= set1}")
    print(f"   set2 > set1 (proper superset): {set2 > set1}")
    
    print("\n4. Disjoint sets:")
    disjoint1 = {1, 2}
    disjoint2 = {3, 4}
    print(f"   disjoint1 = {disjoint1}")
    print(f"   disjoint2 = {disjoint2}")
    print(f"   disjoint1.isdisjoint(disjoint2): {disjoint1.isdisjoint(disjoint2)}")
    print(f"   set1.isdisjoint(set3): {set1.isdisjoint(set3)}")

# =============================================================================
# 3. SET METHODS
# =============================================================================

def set_methods_examples():
    """Demonstrate essential set methods."""
    print_section_header("3. SET METHODS")
    
    sample_set = {1, 2, 3}
    print(f"Starting set: {sample_set}")
    
    print_subsection_header("Adding Elements")
    
    # add() method
    print("1. add() - adds single element:")
    sample_set.add(4)
    print(f"   After add(4): {sample_set}")
    
    sample_set.add(3)  # Adding existing element
    print(f"   After add(3) again: {sample_set} (no change)")
    
    # update() method
    print("\n2. update() - adds multiple elements:")
    sample_set.update([5, 6, 7])
    print(f"   After update([5, 6, 7]): {sample_set}")
    
    sample_set.update({8, 9}, [10, 11])
    print(f"   After update({{8, 9}}, [10, 11]): {sample_set}")
    
    print_subsection_header("Removing Elements")
    
    # remove() method
    print("1. remove() - removes element (raises KeyError if not found):")
    sample_set.remove(10)
    print(f"   After remove(10): {sample_set}")
    
    try:
        sample_set.remove(100)
    except KeyError:
        print("   remove(100) raises KeyError - element not found")
    
    # discard() method
    print("\n2. discard() - removes element (no error if not found):")
    sample_set.discard(11)
    print(f"   After discard(11): {sample_set}")
    
    sample_set.discard(100)  # No error
    print(f"   After discard(100): {sample_set} (no error)")
    
    # pop() method
    print("\n3. pop() - removes and returns arbitrary element:")
    popped = sample_set.pop()
    print(f"   Popped element: {popped}")
    print(f"   Set after pop(): {sample_set}")
    
    # clear() method
    print("\n4. clear() - removes all elements:")
    temp_set = {1, 2, 3, 4, 5}
    print(f"   Before clear(): {temp_set}")
    temp_set.clear()
    print(f"   After clear(): {temp_set}")

def set_copy_examples():
    """Demonstrate set copying methods."""
    print_subsection_header("Set Copying")
    
    original = {1, 2, 3, {4, 5}}  # Note: This would cause TypeError
    # Let's use a proper example
    original = {1, 2, 3, 4, 5}
    
    print(f"Original set: {original}")
    
    # Shallow copy
    copied = original.copy()
    print(f"Copied set: {copied}")
    
    # Modify original
    original.add(6)
    print(f"After adding 6 to original:")
    print(f"  Original: {original}")
    print(f"  Copied: {copied}")
    
    # Assignment vs copy
    print("\nAssignment vs Copy:")
    assigned = original
    copied2 = original.copy()
    
    original.add(7)
    print(f"After adding 7 to original:")
    print(f"  Original: {original}")
    print(f"  Assigned: {assigned} (same object)")
    print(f"  Copied: {copied2} (different object)")

# =============================================================================
# 4. SET COMPREHENSIONS
# =============================================================================

def set_comprehensions_examples():
    """Demonstrate set comprehensions."""
    print_section_header("4. SET COMPREHENSIONS")
    
    print("Set comprehensions provide an elegant way to create sets")
    print("Syntax: {expression for item in iterable if condition}")
    
    print_subsection_header("Basic Set Comprehensions")
    
    # Simple comprehension
    squares = {x**2 for x in range(1, 6)}
    print(f"Squares: {{x**2 for x in range(1, 6)}} = {squares}")
    
    # With condition
    even_squares = {x**2 for x in range(1, 11) if x % 2 == 0}
    print(f"Even squares: {{x**2 for x in range(1, 11) if x % 2 == 0}} = {even_squares}")
    
    # String manipulation
    words = ["hello", "world", "python", "sets"]
    upper_words = {word.upper() for word in words}
    print(f"Uppercase: {{word.upper() for word in words}} = {upper_words}")
    
    # Length filtering
    long_words = {word for word in words if len(word) > 4}
    print(f"Long words: {{word for word in words if len(word) > 4}} = {long_words}")
    
    print_subsection_header("Advanced Set Comprehensions")
    
    # Nested iteration
    pairs = {(x, y) for x in [1, 2] for y in [3, 4]}
    print(f"Pairs: {{(x, y) for x in [1, 2] for y in [3, 4]}} = {pairs}")
    
    # Set of characters from multiple strings
    sentences = ["hello world", "python programming", "set comprehension"]
    unique_chars = {char for sentence in sentences for char in sentence if char.isalpha()}
    print(f"Unique letters from sentences: {unique_chars}")
    
    # Mathematical operations
    pythagorean_triples = {(a, b, c) for a in range(1, 15) 
                          for b in range(a, 15) 
                          for c in range(b, 15) 
                          if a**2 + b**2 == c**2}
    print(f"Pythagorean triples: {pythagorean_triples}")

# =============================================================================
# 5. SET ITERATION
# =============================================================================

def set_iteration_examples():
    """Demonstrate various ways to iterate through sets."""
    print_section_header("5. SET ITERATION TECHNIQUES")
    
    sample_set = {"apple", "banana", "cherry", "date", "elderberry"}
    numbers_set = {1, 2, 3, 4, 5}
    
    print(f"Sample set: {sample_set}")
    print(f"Numbers set: {numbers_set}")
    
    print_subsection_header("Basic Iteration")
    
    # Simple iteration
    print("1. Simple for loop:")
    for item in sample_set:
        print(f"   {item}")
    
    print("\n2. Using enumerate (note: sets are unordered):")
    for i, item in enumerate(sample_set):
        print(f"   {i}: {item}")
    
    print_subsection_header("Conditional Iteration")
    
    # Filtering during iteration
    print("3. Conditional iteration:")
    for item in sample_set:
        if len(item) > 5:
            print(f"   Long fruit: {item}")
    
    print("\n4. List comprehension with sets:")
    long_fruits = [fruit for fruit in sample_set if len(fruit) > 5]
    print(f"   Long fruits: {long_fruits}")
    
    print_subsection_header("Mathematical Operations During Iteration")
    
    # Operations on numeric sets
    print("5. Mathematical operations:")
    total = sum(numbers_set)
    print(f"   Sum of numbers: {total}")
    
    squared = [x**2 for x in numbers_set]
    print(f"   Squared numbers: {squared}")
    
    # Using map and filter
    print("\n6. Using map() and filter():")
    doubled = list(map(lambda x: x * 2, numbers_set))
    print(f"   Doubled: {doubled}")
    
    evens = list(filter(lambda x: x % 2 == 0, numbers_set))
    print(f"   Even numbers: {evens}")

# =============================================================================
# 6. SET VS OTHER DATA STRUCTURES
# =============================================================================

def comparison_examples():
    """Compare sets with other data structures."""
    print_section_header("6. SET vs LIST vs TUPLE COMPARISON")
    
    # Performance comparison
    import time
    
    # Sample data
    data = list(range(10000))
    
    print_subsection_header("Performance Comparison")
    
    # List creation
    start_time = time.time()
    test_list = list(data)
    list_time = time.time() - start_time
    
    # Set creation
    start_time = time.time()
    test_set = set(data)
    set_time = time.time() - start_time
    
    # Tuple creation
    start_time = time.time()
    test_tuple = tuple(data)
    tuple_time = time.time() - start_time
    
    print(f"Creation time for 10,000 elements:")
    print(f"  List:  {list_time:.6f} seconds")
    print(f"  Set:   {set_time:.6f} seconds")
    print(f"  Tuple: {tuple_time:.6f} seconds")
    
    # Membership testing
    print("\nMembership testing (searching for element 5000):")
    
    # List membership
    start_time = time.time()
    result = 5000 in test_list
    list_search_time = time.time() - start_time
    
    # Set membership
    start_time = time.time()
    result = 5000 in test_set
    set_search_time = time.time() - start_time
    
    # Tuple membership
    start_time = time.time()
    result = 5000 in test_tuple
    tuple_search_time = time.time() - start_time
    
    print(f"  List:  {list_search_time:.8f} seconds")
    print(f"  Set:   {set_search_time:.8f} seconds (fastest!)")
    print(f"  Tuple: {tuple_search_time:.8f} seconds")
    
    print_subsection_header("Use Case Recommendations")
    
    recommendations = """
    When to use SETS:
    • Need unique elements only
    • Fast membership testing required
    • Mathematical set operations needed
    • Order doesn't matter
    
    When to use LISTS:
    • Need ordered collection
    • Allow duplicate elements
    • Need indexing/slicing
    • Order matters for your application
    
    When to use TUPLES:
    • Need immutable ordered collection
    • Use as dictionary keys
    • Return multiple values from functions
    • Data shouldn't change after creation
    """
    print(recommendations)

# =============================================================================
# 7. ADVANCED SET TECHNIQUES
# =============================================================================

def advanced_set_techniques():
    """Demonstrate advanced set usage patterns."""
    print_section_header("7. ADVANCED SET TECHNIQUES")
    
    print_subsection_header("Removing Duplicates from Data Structures")
    
    # Remove duplicates from list while preserving order (Python 3.7+)
    original_list = [1, 3, 2, 3, 1, 4, 2, 5]
    
    # Method 1: Simple (loses order in older Python versions)
    unique_simple = list(set(original_list))
    print(f"Original: {original_list}")
    print(f"Method 1 - set(): {unique_simple}")
    
    # Method 2: Preserve order
    def remove_duplicates_ordered(seq):
        seen = set()
        result = []
        for item in seq:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result
    
    unique_ordered = remove_duplicates_ordered(original_list)
    print(f"Method 2 - ordered: {unique_ordered}")
    
    # Method 3: Using dict.fromkeys() (Python 3.7+)
    unique_dict_method = list(dict.fromkeys(original_list))
    print(f"Method 3 - dict.fromkeys(): {unique_dict_method}")
    
    print_subsection_header("Set-based Filtering and Data Analysis")
    
    # Finding common elements across multiple lists
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    list3 = [4, 5, 6, 7, 8]
    
    common = set(list1) & set(list2) & set(list3)
    print(f"Lists: {list1}, {list2}, {list3}")
    print(f"Common elements: {common}")
    
    # Finding unique elements in each list
    all_elements = set(list1) | set(list2) | set(list3)
    unique_to_list1 = set(list1) - set(list2) - set(list3)
    print(f"All elements: {all_elements}")
    print(f"Unique to list1: {unique_to_list1}")
    
    print_subsection_header("Practical Applications")
    
    # User permissions example
    admin_permissions = {"read", "write", "delete", "execute"}
    user_permissions = {"read", "write"}
    guest_permissions = {"read"}
    
    print("Permission System Example:")
    print(f"Admin: {admin_permissions}")
    print(f"User:  {user_permissions}")
    print(f"Guest: {guest_permissions}")
    
    # Check if user can delete
    can_delete = "delete" in user_permissions
    print(f"Can user delete? {can_delete}")
    
    # What permissions does user lack?
    missing_permissions = admin_permissions - user_permissions
    print(f"User missing permissions: {missing_permissions}")
    
    # Tag system example
    post1_tags = {"python", "programming", "tutorial"}
    post2_tags = {"python", "data-science", "pandas"}
    post3_tags = {"web", "javascript", "tutorial"}
    
    all_tags = post1_tags | post2_tags | post3_tags
    python_posts = {"post1", "post2"}  # Posts with python tag
    tutorial_posts = {"post1", "post3"}  # Posts with tutorial tag
    
    print(f"\nBlog Tag System:")
    print(f"All tags: {all_tags}")
    print(f"Posts with both python AND tutorial: {python_posts & tutorial_posts}")

# =============================================================================
# 8. FROZEN SETS
# =============================================================================

def frozenset_examples():
    """Demonstrate frozenset usage."""
    print_section_header("8. FROZEN SETS")
    
    print("Frozensets are immutable versions of sets")
    print("They can be used as dictionary keys or set elements")
    
    print_subsection_header("Creating Frozensets")
    
    # Creating frozensets
    regular_set = {1, 2, 3}
    frozen = frozenset([1, 2, 3, 4, 5])
    frozen_from_set = frozenset(regular_set)
    
    print(f"Regular set: {regular_set}")
    print(f"Frozenset: {frozen}")
    print(f"Frozenset from set: {frozen_from_set}")
    print(f"Type: {type(frozen)}")
    
    print_subsection_header("Frozenset Operations")
    
    fs1 = frozenset([1, 2, 3, 4])
    fs2 = frozenset([3, 4, 5, 6])
    
    print(f"fs1 = {fs1}")
    print(f"fs2 = {fs2}")
    
    # All set operations work with frozensets
    print(f"Union: {fs1 | fs2}")
    print(f"Intersection: {fs1 & fs2}")
    print(f"Difference: {fs1 - fs2}")
    print(f"Symmetric difference: {fs1 ^ fs2}")
    
    # Frozensets are hashable
    print_subsection_header("Frozensets as Dictionary Keys")
    
    coordinates = {
        frozenset(['x', 'y']): (10, 20),
        frozenset(['z', 'w']): (30, 40)
    }
    print(f"Dictionary with frozenset keys: {coordinates}")
    
    # Accessing values
    key = frozenset(['x', 'y'])
    print(f"Value for {key}: {coordinates.get(key)}")
    
    print_subsection_header("Immutability Demonstration")
    
    # Try to modify frozenset (this will fail)
    try:
        frozen.add(6)
    except AttributeError as e:
        print(f"Cannot modify frozenset: {e}")
    
    # But you can create new frozensets from operations
    new_frozen = frozen | frozenset([6, 7])
    print(f"Original: {frozen}")
    print(f"New frozenset: {new_frozen}")

# =============================================================================
# 9. PRACTICAL APPLICATIONS
# =============================================================================

def practical_applications():
    """Show real-world applications of sets."""
    print_section_header("9. PRACTICAL APPLICATIONS")
    
    print_subsection_header("1. Data Cleaning and Deduplication")
    
    # Customer email deduplication
    customer_emails = [
        "user1@example.com", "user2@example.com", "user1@example.com",
        "user3@example.com", "user2@example.com", "user4@example.com"
    ]
    
    unique_emails = set(customer_emails)
    print(f"Original emails ({len(customer_emails)}): {customer_emails}")
    print(f"Unique emails ({len(unique_emails)}): {unique_emails}")
    
    duplicates_count = len(customer_emails) - len(unique_emails)
    print(f"Duplicates removed: {duplicates_count}")
    
    print_subsection_header("2. Inventory and Stock Management")
    
    # Available products
    store_a_products = {"laptop", "mouse", "keyboard", "monitor", "speakers"}
    store_b_products = {"laptop", "tablet", "headphones", "monitor", "webcam"}
    
    # Products available in both stores
    common_products = store_a_products & store_b_products
    print(f"Store A: {store_a_products}")
    print(f"Store B: {store_b_products}")
    print(f"Available in both: {common_products}")
    
    # Products unique to each store
    only_in_a = store_a_products - store_b_products
    only_in_b = store_b_products - store_a_products
    print(f"Only in Store A: {only_in_a}")
    print(f"Only in Store B: {only_in_b}")
    
    print_subsection_header("3. Access Control and Security")
    
    # User role management
    admin_roles = {"create_user", "delete_user", "view_logs", "backup_data"}
    editor_roles = {"edit_content", "publish_content", "view_analytics"}
    viewer_roles = {"view_content", "view_public_analytics"}
    
    # User permissions
    user_permissions = admin_roles | {"special_feature"}
    
    print(f"Admin roles: {admin_roles}")
    print(f"User permissions: {user_permissions}")
    
    # Check specific permissions
    can_delete = "delete_user" in user_permissions
    can_edit = "edit_content" in user_permissions
    
    print(f"Can delete users: {can_delete}")
    print(f"Can edit content: {can_edit}")
    
    print_subsection_header("4. Data Analysis and Filtering")
    
    # Survey response analysis
    responses_group_a = {"satisfied", "very_satisfied", "neutral"}
    responses_group_b = {"dissatisfied", "neutral", "satisfied"}
    responses_group_c = {"very_satisfied", "satisfied", "very_dissatisfied"}
    
    # Find common responses across groups
    common_responses = responses_group_a & responses_group_b & responses_group_c
    print(f"Group A: {responses_group_a}")
    print(f"Group B: {responses_group_b}")
    print(f"Group C: {responses_group_c}")
    print(f"Common across all groups: {common_responses}")
    
    # All possible responses
    all_responses = responses_group_a | responses_group_b | responses_group_c
    print(f"All possible responses: {all_responses}")
    
    print_subsection_header("5. Network and Graph Analysis")
    
    # Social network connections
    alice_friends = {"bob", "charlie", "diana"}
    bob_friends = {"alice", "charlie", "eve"}
    charlie_friends = {"alice", "bob", "frank"}
    
    # Mutual friends
    alice_bob_mutual = alice_friends & bob_friends
    print(f"Alice's friends: {alice_friends}")
    print(f"Bob's friends: {bob_friends}")
    print(f"Mutual friends: {alice_bob_mutual}")
    
    # Potential new connections (friends of friends)
    alice_potential = (bob_friends | charlie_friends) - alice_friends - {"alice"}
    print(f"Alice's potential new friends: {alice_potential}")

# =============================================================================
# 10. PERFORMANCE ANALYSIS
# =============================================================================

def performance_analysis():
    """Analyze set performance characteristics."""
    print_section_header("10. SET PERFORMANCE ANALYSIS")
    
    import time
    import sys
    
    sizes = [100, 1000, 10000, 100000]
    
    print_subsection_header("Memory Usage Comparison")
    
    for size in sizes:
        # Create data structures
        test_list = list(range(size))
        test_set = set(range(size))
        test_tuple = tuple(range(size))
        
        # Calculate memory usage (approximate)
        list_size = sys.getsizeof(test_list) + sum(sys.getsizeof(i) for i in test_list[:10])
        set_size = sys.getsizeof(test_set) + sum(sys.getsizeof(i) for i in list(test_set)[:10])
        tuple_size = sys.getsizeof(test_tuple) + sum(sys.getsizeof(i) for i in test_tuple[:10])
        
        print(f"Size {size:,}:")
        print(f"  List:  {list_size:,} bytes")
        print(f"  Set:   {set_size:,} bytes")
        print(f"  Tuple: {tuple_size:,} bytes")
    
    print_subsection_header("Operation Speed Comparison")
    
    # Test with medium-sized collections
    size = 10000
    test_list = list(range(size))
    test_set = set(range(size))
    
    # Membership testing
    search_value = size - 1  # Worst case for list
    
    # List search
    start = time.time()
    for _ in range(1000):
        result = search_value in test_list
    list_time = time.time() - start
    
    # Set search
    start = time.time()
    for _ in range(1000):
        result = search_value in test_set
    set_time = time.time() - start
    
    print(f"Membership testing (1000 iterations, searching for {search_value}):")
    print(f"  List: {list_time:.6f} seconds")
    print(f"  Set:  {set_time:.6f} seconds")
    print(f"  Set is {list_time/set_time:.1f}x faster!")
    
    print_subsection_header("Best Practices for Performance")
    
    best_practices = """
    SET PERFORMANCE BEST PRACTICES:
    
    1. Use sets for membership testing - O(1) average case vs O(n) for lists
    2. Use sets for removing duplicates - faster than other methods
    3. Use frozensets for dictionary keys when you need set-like keys
    4. Convert to set before performing mathematical operations
    5. Use set comprehensions for efficient set creation
    6. Be aware that set operations create new sets (memory consideration)
    7. For very large sets, consider memory usage vs speed trade-offs
    """
    print(best_practices)

# =============================================================================
# MAIN MENU SYSTEM
# =============================================================================

def display_menu():
    """Display the main menu."""
    menu = """
╔══════════════════════════════════════════════════════════════╗
║                    PYTHON SETS GUIDE                        ║
║                     Interactive Menu                         ║
╠══════════════════════════════════════════════════════════════╣
║  1. Set Basics and Creation                                  ║
║  2. Set Operations (Union, Intersection, etc.)               ║
║  3. Set Methods (add, remove, etc.)                          ║
║  4. Set Comprehensions                                       ║
║  5. Set Iteration Techniques                                 ║
║  6. Set vs List vs Tuple Comparison                          ║
║  7. Advanced Set Techniques                                  ║
║  8. Frozen Sets                                              ║
║  9. Practical Applications                                   ║
║ 10. Performance Analysis                                     ║
║                                                              ║
║  0. Exit                                                     ║
╚══════════════════════════════════════════════════════════════╝
    """
    print(menu)

def main():
    """Main function to run the interactive guide."""
    print_section_header("WELCOME TO PYTHON SETS COMPLETE GUIDE")
    print("This interactive guide will teach you everything about Python sets!")
    print("Each section includes explanations, examples, and hands-on demonstrations.")
    
    while True:
        display_menu()
        
        try:
            choice = input("Enter your choice (0-10): ").strip()
            
            if choice == "0":
                print("\nThank you for using the Python Sets Guide!")
                print("Happy coding with sets! 🐍✨")
                break
            elif choice == "1":
                run_example(set_creation_examples)
                run_example(set_properties_examples)
            elif choice == "2":
                run_example(set_operations_examples)
                run_example(set_comparison_examples)
            elif choice == "3":
                run_example(set_methods_examples)
                run_example(set_copy_examples)
            elif choice == "4":
                run_example(set_comprehensions_examples)
            elif choice == "5":
                run_example(set_iteration_examples)
            elif choice == "6":
                run_example(comparison_examples)
            elif choice == "7":
                run_example(advanced_set_techniques)
            elif choice == "8":
                run_example(frozenset_examples)
            elif choice == "9":
                run_example(practical_applications)
            elif choice == "10":
                run_example(performance_analysis)
            else:
                print("Invalid choice. Please enter a number between 0 and 10.")
                continue
            
            if choice != "0":
                pause_for_user()
                
        except KeyboardInterrupt:
            print("\n\nExiting guide. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()