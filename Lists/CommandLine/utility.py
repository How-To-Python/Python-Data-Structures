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