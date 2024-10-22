def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    if len(args) != 2:
        return 'Please enter the contact\'s name and phone number.'

    name, phone = args
    if name not in contacts:
        contacts[name] = phone
        return 'Contact added.'
    else:
        return f'Contact with name "{name}" already exist.'


def change_contact(args, contacts):
    if len(args) != 2:
        return 'Please enter the contact\'s name and new phone number.'

    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return 'Contact changed.'
    else:
        return f'{name} is not in the contact list.'


def get_contact_phone(args, contacts):
    if len(args) != 1:
        return 'Please enter the contact\'s name.'

    name = args[0]
    return contacts.get(name, f'{name} not found in the contact list.')


def get_all_contacts(contacts):
    if contacts:
        return '\n'.join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return 'The contact list is empty.'


def main():
    contacts = {}
    print('Welcome to the assistant bot!')
    while True:
        user_input = input('Enter a command: ')

        if not user_input:
            print("Please enter a valid command.")
            continue

        command, *args = parse_input(user_input)
        match command:
            case 'close' | 'exit':
                print('Good bye!')
                break
            case 'hello':
                print('How can I help you?')
            case 'add':
                print(add_contact(args, contacts))
            case 'change':
                print(change_contact(args, contacts))
            case 'phone':
                print(get_contact_phone(args, contacts))
            case 'all':
                print(get_all_contacts(contacts))
            case _:
                print('Invalid command.')


if __name__ == '__main__':
    main()
