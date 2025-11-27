from .employee import Employee

class ContractEmployee(Employee):
    """Employee paid based on the number of billable hours worked."""

    def __init__(self, name: str, employee_id: int, hourly_rate: float, hours_worked: float):
        """Capture hourly billing rate and the number of hours worked."""
        super().__init__(name, employee_id, "Contract")
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    @property
    def hourly_rate(self):
        """Return the agreed hourly billing rate."""
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, value):
        if value < 0:
            raise ValueError("Hourly rate cannot be negative.")
        self._hourly_rate = value

    @property
    def hours_worked(self):
        """Return the total billable hours."""
        return self._hours_worked

    @hours_worked.setter
    def hours_worked(self, value):
        if value < 0:
            raise ValueError("Hours worked cannot be negative.")
        self._hours_worked = value

    def compute_salary(self):
        """Calculate pay based on hours and rate."""
        return self.hourly_rate * self.hours_worked
