from pokus4 import jaccardova_vzdalenost_mnozin
from levestein import levensteinova_vzdalenost

def deduplikace_dotazu(dotazy):
    """
    tato funkce spocita jaccardovu vzdalenost a levensteinovu vzadelnost a vyradi z seznamu dotazy, polozky, ktere budou mit
    jaccardovu vzdalenost mensi nez 0.5 a levensteinovu vzdalenost <= 1
    """
    i = 0
    while i < len(dotazy):
        dotaz1 = dotazy[i]
        j = i + 1
        while j < len(dotazy):
            dotaz2 = dotazy[j]
            jaccard = jaccardova_vzdalenost_mnozin(dotaz1["serp"], dotaz2["serp"])
            levenstein = levensteinova_vzdalenost(dotaz1["dotaz"], dotaz2["serp"])
            if jaccard < 0.5 or levenstein <= 1
                dotazy.pop(j)
            else:
                j += 1
        i += 1
    return dotazy


if __name__ == "__main__":

    dotaz1 = {
        "dotaz": "seznam",
        "serp": ["https://www.seznam.cz", "https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz", "https://www.google.com"]
    }
    dotaz2 = {
        "dotaz": "seznamka",
        "serp": ["https://www.seznam.cz", "https://www.google.com", "https://www.novinky.cz", "https://www.idnes.cz", "https://www.zpravy.cz", "https://www.tn.cz"]
    }
    dotaz3 = {
        "dotaz": "sesnam",
        "serp": ["https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz"]
    }
    print(deduplikace_dotazu([dotaz1, dotaz2, dotaz3]))