# src/employee_payroll_tracker/main.py

from src.employee_payroll_tracker.services.payroll_service import PayrollService
from src.employee_payroll_tracker.utils.menus.main_menu import show_main_menu

def main():
    """Entry point that wires the payroll service to the CLI menus."""
    payroll = PayrollService()
    show_main_menu(payroll)

if __name__ == "__main__":
    main()
