def cislo_text(cislo):
    cislo = int(cislo)
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    small_numbers = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    larger_numbers = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
    desitky = ["","", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    


    if cislo < 0 or cislo > 100:
        return "Číslo mimo dosah"
    if cislo < 10:
        return small_numbers[cislo]
    elif cislo < 20:
        return larger_numbers[cislo - 10]
    elif cislo < 100:
        zaokrouhleni = cislo // 10 #zaokrouhlí výsledek dolů
        zbytek = cislo % 10 #zbytek
        if zbytek == 0:
            return desitky[zaokrouhleni]
        else:
            return desitky[zaokrouhleni] + " " + small_numbers[zbytek]
    elif cislo == 100:
        return "sto"
    elif cislo == 0:
        return "nula"
    


if __name__ == "__main__":
    cislo = int(input("Zadej číslo: "))
    text = cislo_text(cislo)
    print(text)