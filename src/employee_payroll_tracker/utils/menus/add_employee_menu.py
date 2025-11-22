# src/employee_payroll_tracker/utils/menus/add_employee_menu.py

from employee_payroll_tracker.utils.validators import validate_float
from employee_payroll_tracker.utils.helpers import pause
from employee_payroll_tracker.models.fulltime import FullTimeEmployee
from employee_payroll_tracker.models.contract import ContractEmployee
from employee_payroll_tracker.models.intern import Intern


def add_fulltime_menu(payroll):
    name = input("Name: ")
    emp_id = input("Employee ID: ")
    base_salary = validate_float("Base salary: ")
    bonus = validate_float("Bonus: ")
    taxes = validate_float("Tax rate (%): ")

    emp = FullTimeEmployee(
        name=name,
        employee_id=emp_id,
        base_salary=base_salary,
        bonus=bonus,
        tax_rate=taxes,
    )

    payroll.add_employee(emp)
    print("Full-time employee added.")
    pause()


def add_contract_menu(payroll):
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
    name = input("Name: ")
    emp_id = input("Employee ID: ")
    stipend = validate_float("Monthly stipend: ")

    emp = Intern(name=name, employee_id=emp_id, monthly_stipend=stipend)
    payroll.add_employee(emp)

    print("Intern added.")
    pause()
