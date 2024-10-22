"""
    Funkce overi, zda zadane cislo je nebo neni prvocislo a vrati True nebo False

    Prvocislo je takove cislo vetsi nez 1, ktere neni delitelne zadnym jinym cislem jenom 1 a samo sebou.

    Napoveda jak otestova prvocislo:
    Cislo 36 vznikne nasobenim:
    1 * 36
    2 * 18
    3 * 12
    4 * 9
    6 * 6
    9 * 4
    12 * 3
    18 * 2
    36 * 1
    Jak vidite v druhe polovine se dvojice opakuji, tzn. v tomto pripade staci overit delitelnost pouze do 6 (vcetne)
    """

def je_prvocislo(cislo):
    if cislo < 2:
        return False
    for i in range(2, cislo):
        if cislo % i == 0:
            return False
    return True

print(f"Číslo: 1 je prvočíslo: {je_prvocislo(1)}")   
print(f"Číslo: 2 je prvočíslo: {je_prvocislo(2)}")
print(f"Číslo: 3 je prvočíslo: {je_prvocislo(3)}")    
print(f"Číslo: 100 je prvočíslo: {je_prvocislo(100)}")
print(f"Číslo: 101 je prvočíslo: {je_prvocislo(101)}")


def vrat_prvocisla(maximum):
    """
    Funkce spočítá všechna prvočísla v rozsahu 1 až maximum a vrátí je jako seznam.
    """
    prvocisla = []
    for i in range(2, maximum + 1):
        if je_prvocislo(i):
            prvocisla.append(i)
    return prvocisla

if __name__ == "__main__":
    cislo = int(input("Zadej maximum: "))
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)