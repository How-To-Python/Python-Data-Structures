from utility import print_section_header, pause_for_user, run_example
from toc import show_table_of_contents
from list_beginner import list_basics, list_slicing_demo, basic_operations
from list_intermediate import list_methods, list_comprehensions, nested_list_comprehensions,iteration_techniques, range_and_indices
from list_advance import list_manipulation_advanced, advanced_techniques
from list_functions import list_functions
from list_advance import advanced_techniques, list_manipulation_advanced
from nested_list import nested_lists, matrix_operations
from performance_tips import performance_tips
from real_examples import real_world_examples, todo_list_example
from interactive_demo import interactive_demonstrations
from list_quick_reference import quick_reference, common_pitfalls



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