creds = {
    'email': 'elliot@pourmand.com',
    'token': 'BwH2F6R2LT5VoPdqCaN6rxqqiCieec1yVZuZBZ0J',
    'subdomain': 'elliotvilhelm'
}


def print_ticket_info(ticket):
    print("Subject: ", ticket.subject)
    print("Description", ticket.description)
    print("ID: ", ticket.id)
    print("Created at: ", ticket.created_at)
    print("Type: ", ticket.type)
    print("Priority: ", ticket.priority)
    print('-' * 40)
    print('\n')


def print_ticket_info_short(ticket):
    print("Subject: ", ticket.subject)
    print("Description", ticket.description)
    print("Priority: ", ticket.priority)
    print('-' * 40)
    print('\n')


def get_tickets():
    found_tickets = []
    for t in zenpy_client.search(type='ticket'):
        found_tickets.append(t)
    return found_tickets


if __name__ == "__main__":
    from zenpy import Zenpy
    from zenpy.lib.exception import APIException
    import sys

    # Check for API Availibility
    try:
        zenpy_client = Zenpy(**creds)
        tickets = get_tickets()
    except APIException:
        print("Error connecting to API")
        sys.exit(1)


    run = True
    while run:
        # Diplsay Prompt
        print("\n(V)IEW_ALL (T)ICKET_NUMBER (E)ND (F)ETCH")
        # Get User Input
        choice = input("Enter Choice: ").upper()
        # Case show all tickets
        if choice.upper() == "V":
            print("\nDisplaying All Tickets!\n")
            i = 1
            for t in tickets:
                print('-' * 40)
                print("Ticket: ", i)
                print_ticket_info_short(t)
                i += 1
        # Case print a single ticket
        elif choice.upper() == "T":
            n = int(input("Enter Ticket Number: "))
            if n > len(tickets):
                print("Ticket Number Out of Range")
            else:
                print("\n")
                print('-' * 40)
                print("Ticket: ", n)
                print_ticket_info(tickets[n-1])
        # Re-fetch tickets
        elif choice.upper() == "F":
            print("Requesting all tickets")
            tickets = get_tickets()
        # Case End program
        elif choice.upper() == "E":
            run = False
            print("Ending Program")
        else:
            print("Invalid choice")