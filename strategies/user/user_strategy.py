from abc import ABC, abstractmethod

class UserStrategy(ABC):
    @abstractmethod
    def display_menu(self):
        pass
    
    @abstractmethod
    def dashboard(self):
        pass

    def generate_ticket(self):
        pass

    def make_payment(self):
        pass

    def generate_invoice(self):
        pass