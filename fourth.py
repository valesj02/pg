def je_tah_mozny(figura, cilova_pozice, obsazene_pozice):
    typ_figury = figura["typ"]
    startovni_pozice = figura["pozice"]

    if not (1 <= cilova_pozice[0] <= 8 and 1 <= cilova_pozice[1] <= 8):
        return False

    if cilova_pozice in obsazene_pozice:
        return False

    radek_start, sloupec_start = startovni_pozice
    radek_cil, sloupec_cil = cilova_pozice

    rozdil_radek = radek_cil - radek_start
    rozdil_sloupec = sloupec_cil - sloupec_start

    if typ_figury == 'pěšec':
        if sloupec_start == sloupec_cil:  
            if rozdil_radek == 1:  
                return True  
            elif radek_start == 2 and rozdil_radek == 2: 
                if (radek_start + 1, sloupec_start) not in obsazene_pozice:
                    return True  
        return False 

    elif typ_figury == 'jezdec':
        if (rozdil_radek, rozdil_sloupec) in [
            (2, 1), (1, 2), (-2, 1), (-1, 2),
            (2, -1), (1, -2), (-2, -1), (-1, -2)
        ]:
            return True  
        return False  

    elif typ_figury == 'věž':
        if radek_start == radek_cil:  
            krok = 1 if sloupec_cil > sloupec_start else -1 
            for sloupec in range(sloupec_start + krok, sloupec_cil, krok):
                if (radek_start, sloupec) in obsazene_pozice:
                    return False  
            return True  
        elif sloupec_start == sloupec_cil:  
            krok = 1 if radek_cil > radek_start else -1 
            for radek in range(radek_start + krok, radek_cil, krok):
                if (radek, sloupec_start) in obsazene_pozice:
                    return False  
            return True  
        return False 

    elif typ_figury == 'střelec':
        if rozdil_radek == rozdil_sloupec or rozdil_radek == -rozdil_sloupec:
            if radek_cil > radek_start:
                krok_radek = 1  
            else:
                krok_radek = -1  

            if sloupec_cil > sloupec_start:
                krok_sloupec = 1
            else:
                krok_sloupec = -1  

            for i in range(1, abs(rozdil_radek)):
                mezipozice = (radek_start + i * krok_radek, sloupec_start + i * krok_sloupec)
                if mezipozice in obsazene_pozice:
                    return False 

            return True 
        return False 

    elif typ_figury == 'dáma':
        if radek_start == radek_cil or sloupec_start == sloupec_cil:
            if radek_start == radek_cil:  
                krok = 1 if sloupec_cil > sloupec_start else -1  
                for sloupec in range(sloupec_start + krok, sloupec_cil, krok):
                    if (radek_start, sloupec) in obsazene_pozice:
                        return False  
                return True  
            elif sloupec_start == sloupec_cil: 
                krok = 1 if radek_cil > radek_start else -1  
                for radek in range(radek_start + krok, radek_cil, krok):
                    if (radek, sloupec_start) in obsazene_pozice:
                        return False  
                return True  
        elif rozdil_radek == rozdil_sloupec or rozdil_radek == -rozdil_sloupec:
            if radek_cil > radek_start:
                krok_radek = 1 
            else:
                krok_radek = -1  

            if sloupec_cil > sloupec_start:
                krok_sloupec = 1  
            else:
                krok_sloupec = -1  

           
            for i in range(1, abs(rozdil_radek)):
                mezipozice = (radek_start + i * krok_radek, sloupec_start + i * krok_sloupec)
                if mezipozice in obsazene_pozice:
                    return False 
            return True  
        return False  

    elif typ_figury == 'král':
        if (rozdil_radek in [-1, 0, 1]) and (rozdil_sloupec in [-1, 0, 1]):
            return True  
        return False  
    return False 


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice)) 
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  
