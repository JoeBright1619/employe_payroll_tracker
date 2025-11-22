from .employee import Employee

class FullTimeEmployee(Employee):
    def __init__(self, name: str, employee_id: int, base_salary: float):
        super().__init__(name, employee_id, "Full-Time")
        self._base_salary = base_salary

    @property
    def monthly_salary(self):
        return self._base_salary

    @monthly_salary.setter
    def monthly_salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self._base_salary = value

    def compute_salary(self):
        return self._base_salary
