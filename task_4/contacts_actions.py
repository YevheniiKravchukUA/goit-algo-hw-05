from error_decorator import input_error

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error     
def update_cantact(args, contacts):
    name, phone = args
    for contact in contacts.keys():
        if contact == name:
            contacts[name] = phone
            return "The contact number has been successfully changed."

@input_error
def show_contact(args, contacts):
    name = args[0]
    for contact in contacts.keys():
        if contact == name:
            return contacts.get(name)
        else:
            return "Not found!"

def show_all_contacts(contacts):
    return contacts