import datetime

class Ticket:
    ticket_id = 0

    def __init__(self, vehicle, spot, parking_attenand) :
        self.ticket_number = Ticket.ticket_id
        self.vehicle = vehicle
        self.time = datetime.datetime.now()
        self.spot = spot
        self.issued_by = parking_attenand
    
    def create_ticket(self, vehicle, spot, parking_attendant):
        return self.__init__(vehicle, spot, parking_attendant)
