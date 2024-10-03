def stars_while():
    print("zacatek")
    i = 0

    while i < 5:
        print("")
        i += 1

    print("konec")
stars_while()


def stars_for():
    print('zacatek')

    for i in [0,1,2,3,4]:
        print("*", i)
    print("konec")


stars_for()



#funkce urcujici, zda number lezi mezi min_number a max_number
def in_range(min_number, max_number, number):
    if (number > min_number and number < max_number):
        print("is in range")
    else:
        print("is not in range")
in_range(100, 1000, 200)

#funkce vrati  string "ahoj jmeno"
#def dopln_jmeno(jmeno):
#
#    jm = input("zadej jmeno: ")
#    print("Ahoj ",jmeno)
#dopln_jmeno(jm)