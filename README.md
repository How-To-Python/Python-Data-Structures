# 🐍 Python Dictionary Guide


- [Creating Dictionaries](./Notebooks/Creating_Dictionaries.ipynb)
    - Create empty dictionaries
    - Create Dictionaries With Values
- [Adding To Dictionaries](./Notebooks/Adding_To_Dictionaries.ipynb)
    - bracket notation, `update()`, `**` operator, `setdefault()`
- [Removing Dictionary Items](./Notebooks/Removing_Dictionary_Items.ipynb)
    - `del()`, `pop()`, `popitem()`, `clear()`, conditional and safe removal techniques
- [Accessing Dictionary Items](./Notebooks/Accessing_Dictionary_Items.ipynb)
    - bracket notation, check if key and/or value exists `.get()`, `.keys()`, `.values()`, `.items()`
- [Accessing Dictionary Items Using Dot Notation](./Notebooks/Access_Dictionary_DotNotation.ipynb)
    - ways to achieve dot notation access for dictionary-like objects
- [Methods and Operations](./Notebooks/Dictionary_Methods_Operations.ipynb)
- [Items Method](./Notebooks/Items_Method.ipynb)
    - used to get key-value pairs from a dictionary as tuples in a view object
- [Keys Method](./Notebooks/Keys_Method.ipynb)
    - used to get the keys of the dictionary
- [Values Method](./Notebooks/Values_Method.ipynb)
    - used to get all the values from a dictionary
- [Dictionary Comprehensions](./Notebooks/Dictionary_Comprehensions.ipynb)
- [Iteration Techniques](./Notebooks/Dictionary_Iteration_Techniques.ipynb)
- [Copying Methods](./Notebooks/Dictionary_Copying_Methods.ipynb)
- [Merging and Updating](./Notebooks/Dictionary_Merging_Updating.ipynb)
    - `update()`
    - `**` operator
- [Set Like Operations on Views](./Notebooks/Dictionary_SetLike_Operations.ipynb)
- [Dictionary Comparison](./Notebooks/Dictionary_Comparison.ipynb)
- [Dictionary Performance](./Notebooks/Dictionary_Performance.ipynb)
- [Dictionary Practice](./Notebooks/Dictionary_Practice_Exercises.ipynb)
- []
- []
- []


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