from models.location import Location

LOCATIONS = [
    Location(1, "Nashville North", "8422 Johnson Pike"),
    Location(2, "Nashville South", "209 Emory Drive")
]

def get_all_locations():
    return LOCATIONS


def get_single_location(id):
    requested_location = None

    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location

    return requested_location


def create_location(location):
    last_location = LOCATIONS[-1]
    new_id = last_location.id + 1
    location["id"] = new_id
    new_location = Location(location['id'], location['name'], location['address'])
    LOCATIONS.append(new_location)
    return location


def delete_location(id):
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            LOCATIONS.pop(index)
            break


def update_location(id, updated_location):
    for index, location in enumerate(LOCATIONS):
        if location.id == id:
            LOCATIONS[index] = Location(updated_location['id'], updated_location['name'], updated_location['address'])
            break
