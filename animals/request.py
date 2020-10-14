import sqlite3
import json

from models.animal import Animal

ANIMALS = [
    Animal(1, "Snickers", "Doing alright", "Dog", 1, 2),
    Animal(2, "Gypsy", "In foster care", "Horse", 1, 2),
    Animal(3, "Blue", "Sleeping as always", "Cat", 2, 2),
]

def get_all_animals():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.customer_id,
            a.location_id
        FROM animal a
        """)

        # Initialize an empty list to hold all animal representations
        animals = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])

            animals.append(animal.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(animals)


def get_single_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.customer_id,
            a.location_id
        FROM animal a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        animal = Animal(data['id'], data['name'], data['breed'], data['status'],
                        data['customer_id'], data['location_id']
                        )

        return json.dumps(animal.__dict__)


def create_animal(animal):
    # Get the id value of the last animal in the list
    last_animal = ANIMALS[-1]
    
    # Add 1 to whatever that number is
    new_id = last_animal.id + 1

    # Add an `id` property to the animal dictionary
    animal["id"] = new_id

    # Add the animal dictionary to the list
    new_animal = Animal(animal['id'], animal['name'], animal['status'], animal['breed'], animal['customer_id'], animal['location_id'])
    ANIMALS.append(new_animal)

    # Return the dictionary with `id` property added/
    return animal

def delete_animal(id):
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            ANIMALS.pop(index)
            break

def update_animal(id, updated_animal):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, animal in enumerate(ANIMALS):
        if animal.id == id:
            # Found the animal. Update the value.
            ANIMALS[index] = Animal(updated_animal['id'], updated_animal['name'], updated_animal['status'], updated_animal['customer_id'], updated_animal['location_id'])
            break