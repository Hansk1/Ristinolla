#Tuodaan käytettävä kirjastot:
import Libary as lib

def paaohjelma():
    #Pelilauta/Ruudukko:
    RUUDUKKO = {
    '1':' ', '2':' ', '3':' ',
    '4':' ', '5':' ', '6':' ',
    '7':' ', '8':' ', '9':' ',
    }
    
    #Alustetaan X aloittamaan peli:
    Vuoro = "X"
    
    VuorojenMaara = 0
    VoittajaLoytynyt = False
    
    #Tulostetaan ruudukon tiedot:
    print("Ruudukon ruudut järjestyksessä ovat:")
    print("1|2|3")
    print("-+-+-")
    print("4|5|6")
    print("-+-+-")
    print("7|8|9")
    print("")
    
    #Tulostetaan pelilauta:
    print("Pelilauta:")
    lib.tulostaRuudukko(RUUDUKKO)
    
    while not VoittajaLoytynyt:
        #Kysytään käyttäjältä ruutu:
        ValittuRuutu = lib.kysyRuutu(Vuoro)
        while True:
            if RUUDUKKO[ValittuRuutu] != " ":
                ValittuRuutu = lib.kysyRuutu("RuutuKaytetty")
            else:
                break
        
        #Syötetään käyttäjän valitsema ruutu ruudukkoon:
        RUUDUKKO[ValittuRuutu] = Vuoro
        
        #Tulostetaan ruudukko:
        lib.tulostaRuudukko(RUUDUKKO)
        
        #Vaihdetaan vuoroa:
        if VuorojenMaara % 2 == 0:
            Vuoro = "O"
        else:
            Vuoro = "X"
        VuorojenMaara += 1

        #Tarkistetaan onko löytynyt voittajaa (Aloitetaan viidennen vuoron kohdalla):
        if VuorojenMaara >= 5:
            VoittajaLoytynyt = lib.tarkistetaanVoitto(RUUDUKKO)
            if VoittajaLoytynyt == True:
                break 
         
        #Tarkistetaan, onko ruudukko täysi ilman voittajaa:    
        if VuorojenMaara == 9:
            print("Ei voittajaa")
            break
        
    #Kysytään käyttäjältä haluaako hän pelata uudestaan:
    Vastaus = input("Haluatko pelata uudestaan(k/e): ")
    print("")
    
    if Vastaus.lower() == "k":
        paaohjelma()
    
    
paaohjelma()
