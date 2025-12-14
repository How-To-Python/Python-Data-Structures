from utility import print_section_header, print_subsection_header
# =============================================================================
# 11. INTERACTIVE DEMONSTRATIONS
# =============================================================================

def interactive_demonstrations():
    """Provide interactive examples for hands-on learning."""
    print_section_header("11. INTERACTIVE DEMONSTRATIONS")
    
    print_subsection_header("Demo 1: List Builder")
    
    def list_builder_demo():
        print("🛠️ Interactive List Builder")
        print("Build a list step by step and see the results!")
        
        my_list = []
        
        operations = [
            ("Add 'apple'", lambda: my_list.append('apple')),
            ("Add 'banana'", lambda: my_list.append('banana')),
            ("Insert 'orange' at index 1", lambda: my_list.insert(1, 'orange')),
            ("Extend with ['grape', 'kiwi']", lambda: my_list.extend(['grape', 'kiwi'])),
            ("Remove 'banana'", lambda: my_list.remove('banana')),
            ("Pop last element", lambda: my_list.pop()),
            ("Sort the list", lambda: my_list.sort()),
            ("Reverse the list", lambda: my_list.reverse())
        ]
        
        for description, operation in operations:
            print(f"\n{description}")
            operation()
            print(f"Result: {my_list}")
    
    list_builder_demo()
    
    print_subsection_header("Demo 2: List Comprehension Workshop")
    
    def comprehension_workshop():
        print("🎯 List Comprehension Workshop")
        
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(f"Starting with: {numbers}")
        
        examples = [
            ("Squares", [x**2 for x in numbers]),
            ("Even numbers only", [x for x in numbers if x % 2 == 0]),
            ("Odd squares", [x**2 for x in numbers if x % 2 == 1]),
            ("Numbers > 5, doubled", [x*2 for x in numbers if x > 5]),
            ("Even/Odd labels", ["even" if x % 2 == 0 else "odd" for x in numbers[:5]])
        ]
        
        for description, result in examples:
            print(f"\n{description}: {result}")
    
    comprehension_workshop()
    
    print_subsection_header("Demo 3: Data Transformation Pipeline")
    
    def transformation_pipeline():
        print("🔄 Data Transformation Pipeline")
        
        # Sample messy data
        messy_data = [
            "  John Doe, 25, Engineer  ",
            "jane smith,30,designer",
            "BOB JOHNSON, 35, MANAGER",
            "",
            "alice brown,28,developer",
            None,
            "charlie davis,32,analyst"
        ]
        
        print("Original messy data:")
        for i, item in enumerate(messy_data):
            print(f"  {i}: {repr(item)}")
        
        # Transformation steps
        print("\n🔧 Transformation steps:")
        
        # Step 1: Filter out None and empty
        step1 = [item for item in messy_data if item and str(item).strip()]
        print(f"1. Remove None/empty: {len(step1)} items")
        
        # Step 2: Clean and split
        step2 = [item.strip().split(',') for item in step1]
        print(f"2. Split by comma: {step2}")
        
        # Step 3: Clean each field and create structured data
        step3 = []
        for person_data in step2:
            if len(person_data) == 3:
                name = person_data[0].strip().title()
                age = int(person_data[1].strip())
                job = person_data[2].strip().title()
                step3.append({"name": name, "age": age, "job": job})
        
        print("3. Create structured data:")
        for person in step3:
            print(f"   {person}")
        
        # Step 4: Analysis
        print("\n📊 Analysis:")
        average_age = sum(person["age"] for person in step3) / len(step3)
        print(f"   Average age: {average_age:.1f}")
        print(f"   Youngest: {min(step3, key=lambda p: p['age'])['name']}")
        print(f"   Oldest: {max(step3, key=lambda p: p['age'])['name']}")
        
        # Job distribution
        jobs = [person["job"] for person in step3]
        job_counts = {job: jobs.count(job) for job in set(jobs)}
        print(f"   Job distribution: {job_counts}")
    
    transformation_pipeline()
