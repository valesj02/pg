def bin_to_dec(binarni_cislo):
    """
    Funkce převede binární číslo (jako str nebo int) na desítkovou hodnotu.
    Pokud je vstup neplatný, vrátí None.
    """

    try:
        if not isinstance(binarni_cislo, str):
            binarni_cislo = str(binarni_cislo)
        desitkove_cislo = int(binarni_cislo, 2)
        print(f"Binární číslo {binarni_cislo} = Desítková hodnota {desitkove_cislo}")
        return desitkove_cislo
    except ValueError:
        print(f"Neplatný vstup: {binarni_cislo}")


def test_funkce():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128

test_funkce()
