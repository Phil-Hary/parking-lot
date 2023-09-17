from services import TicketService

class TicketController:
    ticket_service = TicketService()

    def book_ticket(self, vehicle, spot, parking_attendant):
        return self.ticket_service.book_ticket(vehicle, spot, parking_attendant)