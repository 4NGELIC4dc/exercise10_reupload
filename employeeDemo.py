from employeeMain import Employee, Manager, Executive

def main():

    employee = Employee("John Smith", 45000)
    manager = Manager("Jane Doe", 60000, "Widgets")
    executive = Executive("Weird Guy", 90000, "Thingies")

    print(employee)
    print(manager)
    print(executive)

main()