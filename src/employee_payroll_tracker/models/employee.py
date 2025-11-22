from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name: str, employee_id: int, role: str):
        self._name = name
        self._employee_id = employee_id
        self._role = role
        

    @property
    def name(self):
        return self._name

    @property
    def role(self):
        return self._role

    @property
    def employee_id(self):
        return self._employee_id
    
    @abstractmethod
    def compute_salary(self):
        """Implemented by subclasses."""
        pass

    def __str__(self):
        return f"{self.employee_id}: {self.name} ({self.role})"
