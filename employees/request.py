EMPLOYEES = [
    {
        "id": 1,
        "name": "Miles Obrien",
        "location": "Deep Space 9",
        "manager": False,
        "full time": True,
        "hourly rate": 95
    },
    {
        "id": 2,
        "name": "Tom Paris",
        "location": "Delta Quadrant",
        "manager": False,
        "full time": True,
        "hourly rate": 15
    }
]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee