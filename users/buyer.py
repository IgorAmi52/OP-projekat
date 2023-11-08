from users.logged_user import LoggedUser

class Buyer(LoggedUser):
    def reserve_ticket(self):
        print("rezervacija karata")
        
    def check_tickets(self):
        print("pregled karata")
     
    def delete_ticket(self):
        print("ponistavanje karata")
        
       
    
