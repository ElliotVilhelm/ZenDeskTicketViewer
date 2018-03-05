creds = {
    'email': 'elliot@pourmand.com',
    'token': 'BwH2F6R2LT5VoPdqCaN6rxqqiCieec1yVZuZBZ0J',
    'subdomain': 'elliotvilhelm'
}

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
            print('*'*40)
            print("Ticket: ", i)
            print("Subject: ", ticket.subject)
            print("Description", ticket.description)
            print("ID: ", ticket.id)
            print("Created at: ", ticket.created_at)
            print("Type: ", ticket.type)
            print('*'*40)
            print('\n')
            i += 1
    if choice.upper() == "T":
        n = input("Enter Ticket Number: ")
        if int(n) > len(tickets):
            print("Ticket Niumber Out of Range")
        else:
            print(tickets[int(n) - 1])

