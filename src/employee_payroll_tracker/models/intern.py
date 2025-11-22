from .employee import Employee

class Intern(Employee):
    def __init__(self, name: str, employee_id: int, monthly_stipend: float):
        super().__init__(name, employee_id,"Intern")
        self.stipend = monthly_stipend

    @property
    def stipend(self):
        return self._stipend

    @stipend.setter
    def stipend(self, value):
        if value < 0:
            raise ValueError("Stipend cannot be negative.")
        self._stipend = value

    def compute_salary(self):
        return self._stipend
