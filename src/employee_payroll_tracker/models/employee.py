from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name: str, role: str):
        self._name = name
        self._role = role

    @property
    def name(self):
        return self._name

    @property
    def role(self):
        return self._role

    @abstractmethod
    def compute_salary(self):
        """Implemented by subclasses."""
        pass

    def __str__(self):
        return f"{self.name} ({self.role})"
