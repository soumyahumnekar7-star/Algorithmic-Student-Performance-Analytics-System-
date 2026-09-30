

from data_utils import remove_duplicate_students, assign_grade
from array_algo import reverse_list_in_place, partition_students, get_kth_lowest_mark
from performance import generate_random_marks, compare_search_speeds

def show_menu():
    print("\n--- Student Marks Management System ---")
    print("1. Clean Sample Student Dataset (Remove Duplicates)")
    print("2. Run Array Operations (Reverse & Partition)")
    print("3. Find the K-th Lowest Mark")
    print("4. Generate Synthetic Scores (LCG Algorithm)")
    print("5. Benchmark List vs Dict Search Performance")
    print("6. Exit")

def main():
    # Sample starting data
    raw_students = [
        ("2026_01", "Ananya", 88),
        ("2026_02", "Rohan", 95),
        ("2026_01", "Ananya Duplicate", 88),
        ("2026_03", "Karan", 54),
        ("2026_04", "Sanya", 72),
        ("2026_05", "Vikram", 38)
    ]
    
    active_dataset = list(raw_students)

    while True:
        show_menu()
        choice = input("\nSelect an option (1-6): ").strip()
        
        if choice == '1':
            print(f"\nInitial Record Count: {len(active_dataset)}")
            active_dataset = remove_duplicate_students(active_dataset)
            print(f"Clean Record Count: {len(active_dataset)}")
            print("Updated Dataset:")
            for s_id, name, score in active_dataset:
                print(f"  ID: {s_id} | Name: {name:<10} | Score: {score} | Grade: {assign_grade(score)}")

        elif choice == '2':
            scores_only = [item[2] for item in active_dataset]
            reversed_scores = reverse_list_in_place(scores_only)
            print(f"\nOriginal Marks: {scores_only}")
            print(f"Reversed Marks: {reversed_scores}")
            
            cutoff = 60
            above, below = partition_students(active_dataset, cutoff)
            print(f"\nStudents passing threshold (>= {cutoff}):", [s[1] for s in above])
            print(f"Students needing attention (< {cutoff}):", [s[1] for s in below])

        elif choice == '3':
            scores_only = [item[2] for item in active_dataset]
            try:
                k_val = int(input(f"Enter K rank (1 to {len(scores_only)}): "))
                result = get_kth_lowest_mark(scores_only, k_val)
                if result is not None:
                    print(f"The #{k_val} lowest mark in the class is: {result}")
                else:
                    print("Invalid K range selected.")
            except ValueError:
                print("Please enter a valid integer number.")

        elif choice == '4':
            batch_size = 8
            synthetic = generate_random_marks(batch_size)
            print(f"\nGenerated {batch_size} synthetic test scores using LCG:")
            print(synthetic)

        elif choice == '5':
            print("\nRunning search test on 15,000 records...")
            l_time, d_time = compare_search_speeds(15000)
            print(f"List Linear Search Time: {l_time:.6f} seconds")
            print(f"Dict Hash Lookup Time:   {d_time:.6f} seconds")
            if d_time > 0:
                print(f"Result: Dictionary search was about {int(l_time / d_time)}x faster.")

        elif choice == '6':
            print("\nClosing program. Thank you!")
            break
        else:
            print("Invalid input. Please choose a number from 1 to 6.")

if __name__ == "__main__":
    main()
