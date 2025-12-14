from utility import print_section_header, print_subsection_header
# =============================================================================
# 10. REAL-WORLD EXAMPLES
# =============================================================================

def real_world_examples():
    """Demonstrate practical real-world applications."""
    print_section_header("10. REAL-WORLD EXAMPLES")
    
    print_subsection_header("Example 1: Student Grade Management")
    
    # Student data management
    students = [
        {"name": "Alice", "grades": [95, 87, 92, 88]},
        {"name": "Bob", "grades": [78, 85, 80, 83]},
        {"name": "Charlie", "grades": [92, 88, 95, 90]},
        {"name": "Diana", "grades": [87, 91, 89, 94]}
    ]
    
    print("Student Grade Analysis:")
    print("-" * 40)
    
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = sum(grades) / len(grades)
        highest = max(grades)
        lowest = min(grades)
        
        print(f"{name}:")
        print(f"  Grades: {grades}")
        print(f"  Average: {average:.2f}")
        print(f"  Highest: {highest}")
        print(f"  Lowest: {lowest}")
        print(f"  Status: {'Honor Roll' if average >= 90 else 'Good Standing' if average >= 80 else 'Needs Improvement'}")
        print()
    
    # Class statistics
    all_grades = [grade for student in students for grade in student["grades"]]
    class_average = sum(all_grades) / len(all_grades)
    print(f"Class Statistics:")
    print(f"  Total students: {len(students)}")
    print(f"  Class average: {class_average:.2f}")
    print(f"  Highest grade: {max(all_grades)}")
    print(f"  Lowest grade: {min(all_grades)}")
    
    print_subsection_header("Example 2: Shopping Cart System")
    
    # Shopping cart with inventory management
    inventory = {
        "laptop": {"price": 999.99, "stock": 5},
        "mouse": {"price": 29.99, "stock": 20},
        "keyboard": {"price": 79.99, "stock": 15},
        "monitor": {"price": 299.99, "stock": 8}
    }
    
    cart = [
        {"item": "laptop", "quantity": 1},
        {"item": "mouse", "quantity": 2},
        {"item": "keyboard", "quantity": 1}
    ]
    
    print("Shopping Cart Analysis:")
    print("-" * 30)
    
    total_cost = 0
    valid_cart = True
    
    for cart_item in cart:
        item_name = cart_item["item"]
        quantity = cart_item["quantity"]
        
        if item_name in inventory:
            item_info = inventory[item_name]
            price = item_info["price"]
            stock = item_info["stock"]
            
            if quantity <= stock:
                item_total = price * quantity
                total_cost += item_total
                print(f"{item_name.title()}: {quantity} x ${price:.2f} = ${item_total:.2f}")
            else:
                print(f"❌ {item_name.title()}: Not enough stock! (Requested: {quantity}, Available: {stock})")
                valid_cart = False
        else:
            print(f"❌ {item_name.title()}: Item not found!")
            valid_cart = False
    
    print("-" * 30)
    if valid_cart:
        tax = total_cost * 0.08  # 8% tax
        final_total = total_cost + tax
        print(f"Subtotal: ${total_cost:.2f}")
        print(f"Tax (8%): ${tax:.2f}")
        print(f"Total: ${final_total:.2f}")
    else:
        print("❌ Cart contains invalid items. Please review.")
    
    print_subsection_header("Example 3: Data Processing Pipeline")
    
    # Simulating data processing
    raw_data = [
        "  alice@email.com  ",
        "BOB@EMAIL.COM",
        "",
        "charlie@email.com",
        "invalid-email",
        "diana@email.com  ",
        None,
        "eve@email.com"
    ]
    
    print("Data Processing Pipeline:")
    print(f"Raw data: {raw_data}")
    
    # Step 1: Remove None and empty values
    step1 = [item for item in raw_data if item is not None and str(item).strip()]
    print(f"After removing None/empty: {step1}")
    
    # Step 2: Clean whitespace and convert to lowercase
    step2 = [item.strip().lower() for item in step1]
    print(f"After cleaning: {step2}")
    
    # Step 3: Validate email format (simple check)
    step3 = [email for email in step2 if "@" in email and "." in email.split("@")[1]]
    print(f"After validation: {step3}")
    
    # Step 4: Remove duplicates while preserving order
    step4 = []
    seen = set()
    for email in step3:
        if email not in seen:
            step4.append(email)
            seen.add(email)
    
    print(f"Final processed data: {step4}")
    print(f"Processing summary: {len(raw_data)} → {len(step4)} valid emails")

def todo_list_example():
    """Demonstrate a todo list application."""
    print_subsection_header("Example 4: Todo List Manager")
    
    class TodoList:
        def __init__(self):
            self.tasks = []
        
        def add_task(self, task, priority="medium"):
            self.tasks.append({
                "task": task,
                "priority": priority,
                "completed": False,
                "id": len(self.tasks) + 1
            })
            print(f"✅ Added: {task}")
        
        def complete_task(self, task_id):
            for task in self.tasks:
                if task["id"] == task_id:
                    task["completed"] = True
                    print(f"✅ Completed: {task['task']}")
                    return
            print(f"❌ Task {task_id} not found")
        
        def list_tasks(self, show_completed=True):
            if not self.tasks:
                print("No tasks found!")
                return
            
            print("\n📋 Current Tasks:")
            print("-" * 50)
            
            for task in self.tasks:
                if not show_completed and task["completed"]:
                    continue
                
                status = "✓" if task["completed"] else "○"
                priority_icon = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(task["priority"], "⚪")
                
                print(f"{status} [{task['id']}] {priority_icon} {task['task']}")
        
        def get_summary(self):
            total = len(self.tasks)
            completed = len([t for t in self.tasks if t["completed"]])
            pending = total - completed
            
            return {
                "total": total,
                "completed": completed,
                "pending": pending
            }
    
    # Demo the todo list
    todo = TodoList()
    
    # Add some tasks
    todo.add_task("Complete Python list guide", "high")
    todo.add_task("Review code examples", "medium")
    todo.add_task("Write documentation", "medium")
    todo.add_task("Test edge cases", "low")
    
    # Show all tasks
    todo.list_tasks()
    
    # Complete some tasks
    todo.complete_task(1)
    todo.complete_task(3)
    
    # Show updated list
    print("\n📊 Updated Task List:")
    todo.list_tasks()
    
    # Show summary
    summary = todo.get_summary()
    print(f"\n📈 Summary: {summary['completed']}/{summary['total']} completed, {summary['pending']} pending")
