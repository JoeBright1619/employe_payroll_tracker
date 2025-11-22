from .employee import Employee

class Intern(Employee):
    def __init__(self, name: str, stipend: float):
        super().__init__(name, "Intern")
        self.stipend = stipend

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
