from ..helpers import clear_screen, pause
from ..menus.add_employee_menu import (
    add_fulltime_menu,
    add_contract_menu,
    add_intern_menu,
)

def show_main_menu(payroll):
    """Display the interactive menu loop until the user exits."""
    while True:
        clear_screen()
        print("=== Employee Payroll Tracker ===")
        print("1. Add Full-Time Employee")
        print("2. Add Contract Employee")
        print("3. Add Intern")
        print("4. View All Employees")
        print("5. Generate Payroll Report")
        print("6. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_fulltime_menu(payroll)
        elif choice == "2":
            add_contract_menu(payroll)
        elif choice == "3":
            add_intern_menu(payroll)
        elif choice == "4":
            view_employees(payroll)
        elif choice == "5":
            generate_report(payroll)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
            pause()


def view_employees(payroll):
    """Render the current employee list in a simple table."""
    clear_screen()
    print("--- Employee List ---")

    if not payroll.employees:
        print("No employees found.")
    else:
        for emp in payroll.employees:
            print(f"{emp.employee_id} | {emp.name} | {emp.__class__.__name__}")

    pause()


def generate_report(payroll):
    """Display an aggregated payroll report in tabular form."""
    clear_screen()
    print("===== PAYROLL REPORT =====\n")
    report = payroll.generate_payroll_report()

    if not report:
        print("No employees to show.\n")
        pause()
        return

    # table header
    print(f"{'ID':<5} {'Name':<20} {'Role':<15} {'Salary (RWF)':>15}")
    print("-" * 60)

    # table rows
    for item in report:
        print(
            f"{item['id']:<5} {item['name']:<20} {item['role']:<15} {item['salary']:>15,.2f}"
        )

    print()
    pause()

