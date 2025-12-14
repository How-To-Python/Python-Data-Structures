from utility import print_section_header, print_subsection_header

# =============================================================================
# PERFORMANCE TIPS
# =============================================================================

def performance_tips():
    """Demonstrate performance considerations for lists."""
    print_section_header("9. PERFORMANCE TIPS")
    
    print_subsection_header("Efficient List Building")
    
    # ❌ Inefficient: Concatenation in loop
    print("❌ Inefficient concatenation:")
    result = []
    for i in range(5):
        result = result + [i]  # Creates new list each time
    print("Result:", result)
    
    # ✅ Efficient: append() method
    print("✅ Efficient append:")
    result = []
    for i in range(5):
        result.append(i)  # Modifies existing list
    print("Result:", result)
    
    # ✅ Most efficient: List comprehension
    print("✅ Most efficient - list comprehension:")
    result = [i for i in range(5)]
    print("Result:", result)
    
    print_subsection_header("Memory Considerations")
    
    # Large lists - be mindful of memory
    large_list = list(range(1000000))
    print(f"Large list length: {len(large_list)}")
    print(f"Memory tip: Use generators for large datasets when possible")
    
    # Generator vs List
    def show_memory_difference():
        import sys
        
        # List (stores all values in memory)
        list_comp = [x for x in range(1000)]
        list_size = sys.getsizeof(list_comp)
        
        # Generator (stores only the logic)
        gen_comp = (x for x in range(1000))
        gen_size = sys.getsizeof(gen_comp)
        
        print(f"List comprehension size: {list_size} bytes")
        print(f"Generator expression size: {gen_size} bytes")
        print(f"Memory saved: {list_size - gen_size} bytes")
    
    show_memory_difference()
    
    print_subsection_header("Search Performance")
    
    # Linear search vs set lookup
    large_list = list(range(10000))
    search_set = set(large_list)
    
    target = 9999
    
    print(f"Searching for {target}:")
    print(f"In list (linear search): {'Found' if target in large_list else 'Not found'}")
    print(f"In set (hash lookup): {'Found' if target in search_set else 'Not found'}")
    print("💡 Tip: Use sets for frequent membership testing")
    
    print_subsection_header("Best Practices Summary")
    
    best_practices = [
        "Use list comprehensions for simple transformations",
        "Use append() instead of concatenation in loops",
        "Consider generators for large datasets",
        "Use sets for frequent membership testing",
        "Preallocate list size if known: [None] * size",
        "Use extend() to add multiple items efficiently",
        "Use slicing for bulk operations when possible"
    ]
    
    print("🚀 Performance Best Practices:")
    for i, practice in enumerate(best_practices, 1):
        print(f"  {i}. {practice}")
