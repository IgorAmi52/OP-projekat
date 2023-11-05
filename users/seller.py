from users.buyer import Kupac

class Prodavac(Kupac):
    
    def __init__(self):
        print("prodavac")
        
    def rez_karata(self):
        print("rezervacija karata")
        
    def pregled_karata(self):
        print("pregled karata")
     
    def ponis_karata(self):
        print("ponistavanje karata")
        
       