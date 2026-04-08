from Deque_ADT import Deque
from adt_arraystack import ArrayStack

registration = Deque()
waitlist = ArrayStack()

while True:
    command = input("Enter command: ").strip().lower()

    if command == "list":
        print("Registration List:", registration)
        print("Waitlist:", waitlist.get_stack())

    elif command.startswith("register "):
        name = command.split()[1]

        if not registration.is_full():
            registration.add_back(name)
        else:
            waitlist.push(name)

    elif command.startswith("vip "):
        name = command.split()[1]

        if not registration.is_full():
            registration.add_front(name)
        else:
            removed_person = registration.remove_back()
            if removed_person:
                waitlist.push(removed_person)
            registration.add_front(name)

    elif command.startswith("cancel "):
        name = command.split()[1]

        if registration.remove(name):
            if not waitlist.is_empty():
                registration.add_back(waitlist.pop())
        else:
            print(f"{name} is not found.")

    elif command == "exit":
        break

    else:
        print("Invalid command.")