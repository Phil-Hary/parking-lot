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

    def strikethrough(string):
        striked_character = ""

        for character in string:
            striked_character += character + "\u0336"
        
        return striked_character

    def get_icon(icon_type):
        if icon_type == "BLOCKED":
            return "\u25A9"
        elif icon_type == "AVAILABLE":
            return "\u25AF"
        elif icon_type == "OCCUPIED":
            return "\u2592"
