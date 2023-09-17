class ParkingAttendant:
    attendant_counter = 0

    def __init__(self, name):
        ParkingAttendant.attendant_counter += 1
        self.id = ParkingAttendant.attendant_counter
        self.name = name
