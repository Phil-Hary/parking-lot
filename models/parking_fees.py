class ParkingFee:
    parking_fees_map = {}

    def __init__(self, day_type, vehicle_type, per_hour, first_hour, second_hour, third_hour_and_beyond):
        self.day_type = day_type
        self.vehicle_type = vehicle_type
        self.per_hour = per_hour
        self.first_hour = first_hour
        self.second_hour = second_hour
        self.third_hour_and_beyond = third_hour_and_beyond
    
    staticmethod
    def get_parking_fee(self, vehicle_type, day_type, category):
        vehicle_fee_details = self.parking_fees_map.get(vehicle_type, {})
        day_type_based_details = vehicle_fee_details.get(day_type, {})
        return day_type_based_details(category, None)

    staticmethod
    def set_parking_fee(self, vehicle_type, day_type, category, fee):
        vehicle_fee_details = self.parking_fees_map.get(vehicle_type, None)

        if not vehicle_fee_details:
            self.parking_fees_map[vehicle_type] = {
                [day_type]: {
                    [category]: fee
                }
            }

            return

        day_type_based_details = vehicle_fee_details.get(day_type, None)

        if not day_type_based_details:
            vehicle_fee_details[day_type] = {
                [category]: fee
            }

            return 
        
        category_fee = day_type_based_details.get(category, None)

        if not category_fee:
            day_type_based_details[category] = fee
        
        



    staticmethod
    def create_parking_fee(self, day_type, vehicle_type, per_hour, first_hour, second_hour, third_hour_and_beyond):
        self.__init__(day_type, vehicle_type, per_hour, first_hour, second_hour, third_hour_and_beyond)

        ParkingFee.parking_fees_map[vehicle_type.name]


