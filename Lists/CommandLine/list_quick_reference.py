from utility import print_section_header, print_subsection_header
# =============================================================================
# 12. QUICK REFERENCE
# =============================================================================

def quick_reference():
    """Provide a comprehensive quick reference guide."""
    print_section_header("12. QUICK REFERENCE GUIDE")
    
    reference_sections = {
        "🔨 List Creation": [
            "[]                          # Empty list",
            "[1, 2, 3]                  # With elements",
            "list(range(5))             # From range: [0, 1, 2, 3, 4]",
            "list('hello')              # From string: ['h', 'e', 'l', 'l', 'o']",
            "[0] * 5                    # Repeated elements: [0, 0, 0, 0, 0]"
        ],
        
        "📍 Accessing Elements": [
            "lst[0]                     # First element",
            "lst[-1]                    # Last element",
            "lst[1:3]                   # Slice [1, 2]",
            "lst[:3]                    # First 3 elements",
            "lst[::2]                   # Every 2nd element",
            "lst[::-1]                  # Reverse list"
        ],
        
        "➕ Adding Elements": [
            "lst.append(item)           # Add to end",
            "lst.insert(i, item)        # Insert at index",
            "lst.extend(other)          # Add all from other",
            "lst += other               # Concatenate",
            "lst = lst + other          # Create new list"
        ],
        
        "➖ Removing Elements": [
            "lst.remove(item)           # Remove first occurrence",
            "lst.pop()                  # Remove and return last",
            "lst.pop(i)                 # Remove and return at index",
            "del lst[i]                 # Delete at index",
            "lst.clear()                # Remove all"
        ],
        
        "🔍 Searching & Counting": [
            "item in lst                # Check membership",
            "lst.index(item)            # Find index",
            "lst.count(item)            # Count occurrences",
            "lst.index(item, start)     # Find from start index"
        ],
        
        "🔄 Sorting & Reversing": [
            "lst.sort()                 # Sort in place",
            "lst.sort(reverse=True)     # Sort descending",
            "sorted(lst)                # Return sorted copy",
            "lst.reverse()              # Reverse in place",
            "lst[::-1]                  # Return reversed copy"
        ],
        
        "📊 Built-in Functions": [
            "len(lst)                   # Length",
            "max(lst)                   # Maximum value",
            "min(lst)                   # Minimum value",
            "sum(lst)                   # Sum of numbers",
            "all(lst)                   # All truthy?",
            "any(lst)                   # Any truthy?"
        ],
        
        "🔁 Iteration": [
            "for item in lst:           # Simple iteration",
            "for i, item in enumerate(lst):  # With index",
            "for a, b in zip(lst1, lst2):    # Multiple lists",
            "for i in range(len(lst)):       # Index-based"
        ],
        
        "🎯 List Comprehensions": [
            "[x for x in lst]           # Copy list",
            "[x*2 for x in lst]         # Transform",
            "[x for x in lst if x > 0]  # Filter",
            "[f(x) for x in lst if cond(x)]  # Transform + filter"
        ],
        
        "🧮 Common Patterns": [
            "lst1 + lst2                # Concatenate",
            "lst * 3                    # Repeat 3 times",
            "lst.copy()                 # Shallow copy",
            "lst[:]                     # Also shallow copy",
            "list(lst)                  # Convert to list"
        ]
    }
    
    for section_title, items in reference_sections.items():
        print_subsection_header(section_title)
        for item in items:
            print(f"  {item}")
        print()

def common_pitfalls():
    """Show common pitfalls and how to avoid them."""
    print_subsection_header("⚠️ Common Pitfalls")
    
    pitfalls = [
        {
            "title": "Mutable Default Arguments",
            "wrong": "def add_item(item, lst=[]):  # DON'T DO THIS",
            "right": "def add_item(item, lst=None):\n    if lst is None:\n        lst = []",
            "explanation": "Default mutable arguments are shared between function calls"
        },
        {
            "title": "List Multiplication with Mutable Objects",
            "wrong": "matrix = [[0] * 3] * 3  # All rows reference same list!",
            "right": "matrix = [[0] * 3 for _ in range(3)]",
            "explanation": "Multiplication creates references, not copies"
        },
        {
            "title": "Modifying List While Iterating",
            "wrong": "for item in lst:\n    if condition:\n        lst.remove(item)  # Can skip elements",
            "right": "lst = [item for item in lst if not condition]",
            "explanation": "Removing items changes indices during iteration"
        },
        {
            "title": "Confusing append() vs extend()",
            "wrong": "lst.append([1, 2, 3])  # Adds the list as single item",
            "right": "lst.extend([1, 2, 3])  # Adds each item individually",
            "explanation": "append() adds one item, extend() adds multiple items"
        }
    ]
    
    for i, pitfall in enumerate(pitfalls, 1):
        print(f"{i}. {pitfall['title']}")
        print(f"   ❌ Wrong: {pitfall['wrong']}")
        print(f"   ✅ Right: {pitfall['right']}")
        print(f"   💡 Why: {pitfall['explanation']}")
        print()
