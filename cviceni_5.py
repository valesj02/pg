import csv
import sys

def nacti_csv(soubor):
    data = []
    with open(soubor, "r") as file:
        reader = csv.reader(file)
        for radek in reader:
            data.append(radek)
    return data



def spoj_data(*data):
    vysledek = {}
    for d in data:
        for i, v in enumerate(d):
            if i == 0:
                continue
            if v[1] not in vysledek:
                vysledek[v[1]] = 1
            else:
                vysledek[v[1]].extend(v)
    return vysledek


def zapis_csv(soubor, data):
    data = []
    with open(soubor, "w") as file:
        writer = csv.writer(file)
        for radek in writer:
            data.append(radek)
    return data


if __name__ == "__main__":
    try:
        soubor1 = sys.argv[1]
        soubor2 = sys.argv[2]
        csv_data1 = nacti_csv(soubor1)
        csv_data2 = nacti_csv(soubor2)
        print(csv_data1)
        print(csv_data2)
        vysledna_data = spoj_data(csv_data1, csv_data2)
        print(vysledna_data)
        zapis_csv("vysledny_excel.csv", vysledna_data)
    except IndexError:
        print("Zadej 2 vstupní soubory typu csv")
    except FileNotFoundError:
        print("Soubor neexistuje")
