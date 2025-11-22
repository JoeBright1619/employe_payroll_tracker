class PayrollService:
    def __init__(self):
        self.employees = []          # list of Employee objects
        self.employee_map = {}       # id -> Employee object

    def add_employee(self, employee):
        """Add an employee to both structures."""
        if employee.employee_id in self.employee_map:
            raise ValueError("Employee with this ID already exists")

        self.employees.append(employee)
        self.employee_map[employee.employee_id] = employee
        return employee

    def remove_employee(self, employee_id):
        """Remove employee from list + map."""
        if employee_id not in self.employee_map:
            raise ValueError("Employee not found")

        employee = self.employee_map.pop(employee_id)
        self.employees = [e for e in self.employees if e.employee_id != employee_id]
        return employee

    def get_employee(self, employee_id):
        """Fast O(1) lookup."""
        return self.employee_map.get(employee_id)

    def compute_all_salaries(self):
        """Polymorphic salary computation."""
        payroll = {}

        for employee in self.employees:
            payroll[employee.employee_id] = employee.compute_salary()  # polymorphic
            
        return payroll

    def generate_payroll_report(self):
        """Return a readable, role-aware summary."""
        report = []

        for employee in self.employees:
            salary = employee.compute_salary()
            report.append({
                "id": employee.employee_id,
                "name": employee.name,
                "role": employee.__class__.__name__,
                "salary": round(salary, 2)
            })

        return report