from models import Ticket

class TicketService:
    def book_ticket(self, vehicle, spot, parking_attendant):
        return Ticket(vehicle, spot, parking_attendant)

        
