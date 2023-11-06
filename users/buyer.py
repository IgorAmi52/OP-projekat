from users.loged_user import LogedUser

class Buyer(LogedUser):
    
    def __init__(self):
        print("kupac")
        exit()
        
    def reserve_ticket(self):
        print("rezervacija karata")
        
    def check_tickets(self):
        print("pregled karata")
     
    def delete_ticket(self):
        print("ponistavanje karata")
        
       
    
