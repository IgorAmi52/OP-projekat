from korisnik import Korisnik

class Reg_Koris(Korisnik):
    
    korisIme = ''
    sifra = ''
    ime = ''
    prezime = ''
    
    def __init__(self):
        print("registrovani korisnik")
        
    def odjava(self):
        print("odjava reg korisnika")
        
    def izmena_podataka(self):
        print("izmena podataka reg korisnika")