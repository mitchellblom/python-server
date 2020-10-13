from models.customer import Customer

CUSTOMERS = [
    Customer(1, "Hannah Hall", "123 NSS", "foo@bar.com", "willbehashedpw"),
    Customer(2, "Brian Neal", "123 NSS Day", "foo2@bar.com", "willbehashedpw"),
    Customer(3, "Mitchell Blom", "123 NSS Evening", "foo3@bar.com", "willbehashedpw"),
]

def get_all_customers():
    return CUSTOMERS


def get_single_customer(id):
    requested_customer = None
    for customer in CUSTOMERS:
        if customer.id == id:
            requested_customer = customer

    return requested_customer


def create_customer(customer):
    last_customer = CUSTOMERS[-1]
    new_id =  last_customer.id + 1
    customer["id"] = new_id
    new_customer = Customer(customer['id'], customer['name'], customer['address'], customer['email'], customer['password'])
    CUSTOMERS.append(new_customer)
    return customer


def delete_customer(id):
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS.pop(index)
            break


def update_customer(id, updated_customer):
    for index, customer in enumerate(CUSTOMERS):
        if customer.id == id:
            CUSTOMERS[index] = Customer(updated_customer['id'], updated_customer['name'], updated_customer['address'], updated_customer['email'], updated_customer['password'])
            break