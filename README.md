# 🐍 Python Dictionary Guide


1. [Creating Dictionaries](./Notebooks/Creating_Dictionaries.ipynb)
    - Create empty dictionaries
    - Create Dictionaries With Values
2. [Adding To Dictionaries](./Notebooks/Adding_To_Dictionaries.ipynb)
    - bracket notation
    - `update()`
    - `**` operator
    - `setdefault()`
3. [Removing Dictionary Items](./Notebooks/Removing_Dictionary_Items.ipynb)
    - `del()`
    - `pop()`
    - `popitem()`
    - `clear()`
    - conditional and safe removal techniques
4. [Accessing Dictionary Items](./Notebooks/Accessing_Dictionary_Items.ipynb)
    - bracket notation, check if key and/or value exists 
    - `.get()`
    - `.keys()`
    - `.values()`
    - `.items()`
    -  `dir()` function
5. [Items Method](./Notebooks/Items_Method.ipynb)
    - used to get key-value pairs from a dictionary as tuples in a view object
6. [Keys Method](./Notebooks/Keys_Method.ipynb)
    - used to get the keys of the dictionary
7. [Values Method](./Notebooks/Values_Method.ipynb)
    - used to get all the values from a dictionary
8. [Iteration Techniques](./Notebooks/Dictionary_Iteration_Techniques.ipynb)
9. [Copying Methods](./Notebooks/Dictionary_Copying_Methods.ipynb)
    - `copy()` method
    - `dict()` constructor
10. [Merging and Updating](./Notebooks/Dictionary_Merging_Updating.ipynb)
    - `update()`
    - `**` operator
11. [Dictionary Comprehensions](./Notebooks/Dictionary_Comprehensions.ipynb)
12. [Set Like Operations on Views](./Notebooks/Dictionary_SetLike_Operations.ipynb)
    - set operations on keys
    - set operations on items (key-value pairs)
13. [Dictionary Comparison](./Notebooks/Dictionary_Comparison.ipynb)
    - equality comparison
    - comparing nested dictionaries
14. [Accessing Dictionary Items Using Dot Notation](./Notebooks/Access_Dictionary_DotNotation.ipynb)
    - ways to achieve dot notation access for dictionary-like objects
15. [Advance Operations](./Notebooks/Dictionary_Operations_Advanced.ipynb)
    - `fromkeys()` class method
    - mutable defaults
    - filtering and transformation
16. [Dictionary Performance](./Notebooks/Dictionary_Performance.ipynb)
17. [Dictionary Practice](./Notebooks/Dictionary_Practice_Exercises.ipynb)


## Summary

### Essential Dictionary Methods:

**Access Methods:**
- `dict.get(key, default=None)` - Safe access with optional default
- `dict.setdefault(key, default=None)` - Get or set default value
- `dict.keys()`, `dict.values()`, `dict.items()` - View objects

**Modification Methods:**
- `dict.update(other)` - Merge another dictionary or iterable
- `dict.pop(key, default)` - Remove and return value
- `dict.popitem()` - Remove and return last item
- `dict.clear()` - Remove all items

**Utility Methods:**
- `dict.copy()` - Create shallow copy
- `dict.fromkeys(keys, value)` - Create dictionary from keys

### Key Concepts:

1. **View Objects** are dynamic and reflect dictionary changes
2. **Shallow Copy** copies references to nested objects
3. **Set Operations** work on dictionary views (keys, items)
4. **Dictionary Equality** compares all key-value pairs regardless of order
5. **Performance** - `in` operator is typically fastest for existence checks

### Best Practices:

- Use `get()` for safe access instead of direct indexing
- Use `setdefault()` for initialization patterns
- Use `**` operator for modern dictionary merging
- Use view objects for set-like operations
- Be careful with mutable default values in `fromkeys()`



### Dictionary Iteration Methods:

**Basic Iteration:**
- `for key in dict:` - Iterate over keys (default)
- `for key in dict.keys():` - Explicit key iteration
- `for value in dict.values():` - Iterate over values
- `for key, value in dict.items():` - Iterate over key-value pairs

**Enhanced Iteration:**
- `enumerate(dict.items())` - Add index numbers
- `sorted(dict.items())` - Iterate in sorted order
- `sorted(dict.items(), key=lambda x: x[1])` - Sort by values

### Best Practices:

1. **Use `.items()` when you need both keys and values**
2. **Use `.values()` when you only need values (most efficient)**
3. **Use `.keys()` for set operations or when checking multiple keys**
4. **Use `sorted()` for ordered iteration**
5. **Use `enumerate()` when you need position information**
6. **Consider chunking for very large dictionaries**

### Performance Tips:

- `.values()` iteration is fastest when you only need values
- `.items()` is more efficient than separate key/value lookups
- Use list comprehensions/generator expressions for simple transformations
- Consider `itertools` for advanced iteration patterns

### Common Patterns:

- **Filtering**: `for k, v in dict.items() if condition`
- **Transformation**: `{k: transform(v) for k, v in dict.items()}`
- **Aggregation**: `sum(dict.values())`, `max(dict, key=dict.get)`
- **Grouping**: Use `defaultdict(list)` or manual grouping
- **Nested iteration**: Multiple nested loops for complex structures




<!-- ### 📊 Python Data Structures Comparison

| Data Structure | Ordered | Mutable | Duplicates | Indexed | Use Case |
|----------------|---------|---------|------------|---------|----------|
| **List** | ✅ | ✅ | ✅ | Numeric | General sequences |
| **Tuple** | ✅ | ❌ | ✅ | Numeric | Fixed collections |
| **Set** | ❌ | ✅ | ❌ | ❌ | Unique items |
| **Dict** | ✅* | ✅ | ❌ (keys) | Keys | Key-value pairs |
| **String** | ✅ | ❌ | ✅ | Numeric | Text data |

## 🔧 Learning Guide Prerequisites

- **Python 3.6+** installed on your system
- **Basic Python knowledge** (variables, functions, basic syntax)
- **Jupyter Notebook** (optional, for notebook experience)

## 🎓 Learning Materials

- **[Python Dictionaries Command-Line Guide](./CommandLine/python_dictionary_complete_guide.py)**
    - Complete command-line guide with interactive menu system
- **[Python Dictionaries Interactive Guide](./Notebooks/PYTHON_DICTIONARY_INTERACTIVE_NOTEBOOK_GUIDE.md)**
    - Jupyter notebooks with hands-on examples
- **Existing code examples** - Real-world implementations and demonstrations

### 📖 What's Next?

**Explore related topics:**
- **List** - Ordered, Mutable Collections
- **Sets** - Unordered Collections of Unique Elements
- **Tuples** - Immutable Sequences
- **NumPy arrays** - Numerical Computing
- **Pandas** - Data Analysis

**Happy Learning! 🐍✨** -->