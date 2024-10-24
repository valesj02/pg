def levensteinova_vzdalenost(dotaz1, dotaz2):

    length = max(len(dotaz1), len(dotaz2))
    i = 0
    levenstein = 0
    while i < length:
        if i < len(dotaz1) and i < len(dotaz2):
            if dotaz1[i] != dotaz2[i]:
                levenstein += 1
        else:
            levenstein += 1
        i += 1
    return levenstein

    

if __name__ == "__main__":

    query1 = "seznam"
    query2 = "seznamka"
    query3 = "sesnam"

    print(levensteinova_vzdalenost(query1, query2))
    print(levensteinova_vzdalenost(query2, query3))
    print(levensteinova_vzdalenost(query1, query3))