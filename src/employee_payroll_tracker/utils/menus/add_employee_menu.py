# src/employee_payroll_tracker/utils/menus/add_employee_menu.py

from ..validators import validate_float
from ..helpers import pause
from ...models.fulltime import FullTimeEmployee
from ...models.contract import ContractEmployee
from ...models.intern import Intern


def add_fulltime_menu(payroll):
    """Prompt for full-time details and persist the resulting employee."""
    name = input("Name: ")
    emp_id = input("Employee ID: ")
    base_salary = validate_float("Base salary: ")

    emp = FullTimeEmployee(
        name=name,
        employee_id=emp_id,
        base_salary=base_salary,
    )

    payroll.add_employee(emp)
    print("Full-time employee added.")
    pause()


def add_contract_menu(payroll):
    """Capture contract-specific fields and add the employee to payroll."""
    name = input("Name: ")
    emp_id = input("Employee ID: ")
    hourly_rate = validate_float("Hourly rate: ")
    hours_worked = validate_float("Hours worked: ")

    emp = ContractEmployee(
        name=name,
        employee_id=emp_id,
        hourly_rate=hourly_rate,
        hours_worked=hours_worked,
    )

    payroll.add_employee(emp)
    print("Contract employee added.")
    pause()


def add_intern_menu(payroll):
    """Capture intern information and record them in the payroll system."""
    name = input("Name: ")
    emp_id = input("Employee ID: ")
    stipend = validate_float("Monthly stipend: ")

    emp = Intern(name=name, employee_id=emp_id, monthly_stipend=stipend)
    payroll.add_employee(emp)

    print("Intern added.")
    pause()
