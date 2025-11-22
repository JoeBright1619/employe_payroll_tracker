from .employee import Employee

class FullTimeEmployee(Employee):
    def __init__(self, name: str, monthly_salary: float):
        super().__init__(name, "Full-Time")
        self._monthly_salary = monthly_salary

    @property
    def monthly_salary(self):
        return self._monthly_salary

    @monthly_salary.setter
    def monthly_salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self._monthly_salary = value

    def compute_salary(self):
        return self._monthly_salary
