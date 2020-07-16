#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = [None] * length
    curr = {}
    #loop through tickets
    for ticket in tickets:
        #
        curr[ticket.source] = ticket.destination
    next_destination = curr["NONE"]

    for i in range(0, length):
        route[i] = next_destination
        next_destination = curr[next_destination]   
    #print(curr[ticket.source])



    return route
# ticket_1 = Ticket("PIT", "ORD")
# ticket_2 = Ticket("XNA", "SAP")
# ticket_3 = Ticket("SFO", "BHM")
# ticket_4 = Ticket("FLG", "XNA")
# ticket_5 = Ticket("NONE", "LAX")
# tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5]
                       
# reconstruct_trip(tickets, 5)