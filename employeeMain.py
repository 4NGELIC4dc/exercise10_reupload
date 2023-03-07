class Employee:

    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def __repr__(self):
        return self._name + " has a salary of %.2f" % self._salary

class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self._department = department

    def __repr__(self):
        return self._name + " has a salary of %.2f" % self._salary + " and manages the " + \
               self._department + " department."

class Executive(Manager):

    def __init__(self, name, salary, department):
        super().__init__(name, salary, department)

    def __repr__(self):
        return self._name + " has a salary of %.2f" % self._salary + \
               " and is the executive for the " + self._department + " department."

def main():

    employee = Employee("John Smith", 45000)
    manager = Manager("Jane Doe", 60000, "Widgets")
    executive = Executive("Weird Guy", 90000, "Thingies")

    print(employee)
    print(manager)
    print(executive)

main()