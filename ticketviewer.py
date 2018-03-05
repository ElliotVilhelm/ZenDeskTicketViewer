creds = {
    'email': 'elliot@pourmand.com',
    'token': 'BwH2F6R2LT5VoPdqCaN6rxqqiCieec1yVZuZBZ0J',
    'subdomain': 'elliotvilhelm'
}


def print_ticket_info(ticket):
    print('*' * 40)
    print("Ticket: ", int(n))
    print("Subject: ", ticket.subject)
    print("Description", ticket.description)
    print("ID: ", ticket.id)
    print("Created at: ", ticket.created_at)
    print("Type: ", ticket.type)
    print('*' * 40)
    print('\n')


if __name__ == "__main__":
    from zenpy import Zenpy
    zenpy_client = Zenpy(**creds)
    run = True
    while run:
        tickets = []
        # Refresh Tickets
        for ticket in zenpy_client.search(type='ticket'):
            tickets.append(ticket)

        print("\n(V)IEW_ALL (T)ICKET_NUMBER (E)ND")
        choice = input("Enter Choice: ")
        print(choice.upper())
        if choice.upper() == "E":
            run = False
        if choice.upper() == "V":
            i = 1
            for ticket in tickets:
                print_ticket_info(ticket)
        if choice.upper() == "T":
            n = int(input("Enter Ticket Number: "))
            if int(n) > len(tickets):
                print("Ticket Number Out of Range")
            else:
                print_ticket_info(tickets[n-1])