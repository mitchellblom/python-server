from models.employee import Employee

EMPLOYEES = [
    Employee(1, "Miles Obrien", "9 Deep Space", 2),
    Employee(1, "Tom Paris", "44 Delta Quadrant", 1),
]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee


def create_employee(employee):
    last_employee = EMPLOYEES[-1]
    new_id = last_employee.id + 1
    employee["id"] = new_id
    new_employee = Employee(employee['id'], employee['name'], employee['address'], employee['location_id'])
    EMPLOYEES.append(new_employee)
    return employee


def delete_employee(id):
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES.pop(index)
            break


def update_employee(id, updated_employee):
    for index, employee in enumerate(EMPLOYEES):
        if employee.id == id:
            EMPLOYEES[index] = Employee(updated_employee['id'], updated_employee['name'], updated_employee['address'], updated_employee['location_id'])
            break