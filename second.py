def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    small_numbers = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    teens = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
    desitky = ["","", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    
    if cislo < 10:
        return small_numbers[cislo]
    elif cislo < 20:
        return teens[cislo - 10]
    elif cislo < 100:
        desitka = cislo // 10 #zaokrouhlí výsledek dolů
        jednotka = cislo % 10 #zbytek
        if jednotka == 0:
            return desitky[desitka]
        else:
            return desitky[desitka] + " " + small_numbers[jednotka]
    elif cislo == 100:
        return "sto"
    else:
        return "Číslo mimo rozsah"


if __name__ == "__main__":
    cislo = int(input("Zadej číslo: "))
    text = cislo_text(cislo)
    print(text)
