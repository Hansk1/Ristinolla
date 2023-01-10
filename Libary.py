VERSIO = 1.0

def tulostaRuudukko(RUUDUKKO):
    print(RUUDUKKO['1'] + "|" + RUUDUKKO['2'] + "|" + RUUDUKKO['3'])
    print("-+-+-")
    print(RUUDUKKO['4'] + "|" + RUUDUKKO['5'] + "|" + RUUDUKKO['6'])
    print("-+-+-")
    print(RUUDUKKO['7'] + "|" + RUUDUKKO['8'] + "|" + RUUDUKKO['9'])
    print("")
    
    return None



def kysyRuutu(Vuoro):
    if Vuoro == "X":
        Syote = input("X: Vuoro, valitse ruutu: ")
    elif Vuoro == "O":
        Syote = input("O: Vuoro, valitse ruutu: ")
    elif Vuoro == "RuutuKaytetty":
        Syote = input("Valittu ruutu on käytetty, valitse uusi ruutu: ")
    
    return Syote
  
  
  
def tarkistetaanVoitto(Ruudukko):
    if Ruudukko["1"] == Ruudukko["2"] == Ruudukko["3"] != ' ':
        print(Ruudukko["1"] + ": Voitti")
        return True
        
    elif Ruudukko["4"] == Ruudukko["5"] == Ruudukko["6"] != ' ':
        print(Ruudukko["4"] + ": Voitti")
        return True
        
    elif Ruudukko["7"] == Ruudukko["8"] == Ruudukko["9"] != ' ':
        print(Ruudukko["7"] + ": Voitti")
        return True
        
    elif Ruudukko["1"] == Ruudukko["4"] == Ruudukko["7"] != ' ':
        print(Ruudukko["1"] + ": Voitti")
        return True
        
    elif Ruudukko["2"] == Ruudukko["5"] == Ruudukko["8"] != ' ':
        print(Ruudukko["2"] + ": Voitti")
        return True
        
    elif Ruudukko["3"] == Ruudukko["6"] == Ruudukko["9"] != ' ':
        print(Ruudukko["3"] + ": Voitti")
        return True
        
    elif Ruudukko["1"] == Ruudukko["5"] == Ruudukko["9"] != ' ':
        print(Ruudukko["1"] + ": Voitti")
        return True
        
    elif Ruudukko["3"] == Ruudukko["5"] == Ruudukko["7"] != ' ':
        print(Ruudukko["3"] + ": Voitti")
        return True
    
    #Voittajaa ei löytynyt:
    return False
