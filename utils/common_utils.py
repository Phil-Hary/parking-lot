class CommonUtils:
    def get_data_from_user(data):
        user_data = {}

        for field in data:
            valid = False

            while not valid:
                print(f"Enter {field.replace('_', ' ')}")
                user_input = input()

                user_input = user_input.strip()

                if user_input:
                    user_data[field] = user_input
                    valid = True
        
        return user_data
