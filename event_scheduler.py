from Deque_ADT import Deque
from adt_arraystack import ArrayStack

registration= Deque() 
waitlist = ArrayStack() 

while True: 
    command = input('Enter command: ')
    if command == "list":
        print ("Registered attendees: ", registration)
        print ("Waitlist: ", waitlist.get_stack())
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
            waitlist.push(removed_person)
            registration.add_front(name) 
    
    elif command.startswith("cancel "): 
        name = command.split()[1] 

        if registration.remove(name): 
            if not waitlist.is_empty(): 
                next_person = waitlist.pop() 
                registration.add_back(next_person) 
        else: 
            print(f"{name} is not found.") 

    elif command == "exit": 
        break 