import sqlite3
import json
from models.employee import Employee


def get_all_employees():
    with sqlite3.connect("./kennel.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address
        FROM employee e
        """)

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'])
            employees.append(employee.__dict__)

    return json.dumps(employees)


def get_single_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address
        FROM employee e
        WHERE e.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        employee = Employee(data['id'], data['name'], data['address'])

        return json.dumps(employee.__dict__)


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