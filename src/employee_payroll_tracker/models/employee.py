from abc import ABC, abstractmethod

class Employee(ABC):
    """Base type for all employees supported by the payroll system."""

    def __init__(self, name: str, employee_id: int, role: str):
        """Store core identity fields shared across employee types."""
        self._name = name
        self._employee_id = employee_id
        self._role = role
        

    @property
    def name(self):
        """Return the employee's display name."""
        return self._name

    @property
    def role(self):
        """Return the textual representation of the employee's role."""
        return self._role

    @property
    def employee_id(self):
        """Return the unique identifier assigned to the employee."""
        return self._employee_id
    
    @abstractmethod
    def compute_salary(self):
        """Implemented by subclasses."""
        pass

    def __str__(self):
        """Readable representation used by menu views and logs."""
        return f"{self.employee_id}: {self.name} ({self.role})"
