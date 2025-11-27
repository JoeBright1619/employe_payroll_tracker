from .employee import Employee

class Intern(Employee):
    """Employee type used for stipend-based interns."""

    def __init__(self, name: str, employee_id: int, monthly_stipend: float):
        """Set the monthly stipend allocated to the intern."""
        super().__init__(name, employee_id,"Intern")
        self.stipend = monthly_stipend

    @property
    def stipend(self):
        """Return the stipend amount."""
        return self._stipend

    @stipend.setter
    def stipend(self, value):
        if value < 0:
            raise ValueError("Stipend cannot be negative.")
        self._stipend = value

    def compute_salary(self):
        """Return the stipend as the salary proxy."""
        return self._stipend
