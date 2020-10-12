from models.animal import Animal

ANIMALS = [
    Animal(1, "Snickers", "Dog", 1, 4, "Ready for discharge"),
    Animal(2, "Gypsy", "Dog", 1, 2, "Ready for discharge"),
    Animal(3, "Blue", "Cat", 2, 4, "Ready for discharge"),
]

def get_all_animals():
    return ANIMALS

# Function with a single parameter
def get_single_animal(id):
    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if animal.id == id:
            requested_animal = animal

    return requested_animal

def create_animal(animal):
    # Get the id value of the last animal in the list
    last_animal = ANIMALS[-1]
    
    # Add 1 to whatever that number is
    new_id = last_animal.id + 1

    # Add an `id` property to the animal dictionary
    animal["id"] = new_id

    # Add the animal dictionary to the list
    new_animal = Animal(animal['id'], animal['name'], animal['species'], animal['location_id'], animal['customer_id'], animal['status'])
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
            ANIMALS[index] = Animal(updated_animal['id'], updated_animal['name'], updated_animal['species'], updated_animal['location_id'], updated_animal['customer_id'], updated_animal['status'])
            break