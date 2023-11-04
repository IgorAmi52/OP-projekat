from enum import Enum

class Uloge(Enum):
    
    neReg = 'Neregistrovani Kupac'
    reg = 'Registrovani Kupac'
    prod = 'Prodavac'
    men = 'Menadzer'

class Korisnik:
    
    uloga = Uloge.neReg
    
    def __init__(self):
        print("Meni za korisnika obicnog")
    
    def prijava(self):
        print("prijavljivanje")
        
    def izlazak(self):
        print("izlazak")
        
    def pregled_filmova(self):
        print("pregled filmova")
        
    def pretraga(self):
        print("pretraga filma")
        
    def vise_krit_pretraga(self):
        print("vise krit pretraga")
    
        #while dok se korisnik ne uloguje(moze da napravi usera ili da se loguje)

    
    
            
        
        