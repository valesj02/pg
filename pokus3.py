def my_enumerate(iterable, start=0):
    """
    Nase vlastni implementace enumerate()
    """
    results = []
    index = start
    for value in iterable:
        results.append( (index, value) )
        index += 1
    return results


def while_enumerate(iterable, start=0):
    results = []
    i = 0
    while i < len(iterable):
        results.append( (start + i, iterable[i]) )
        i += 1
    return results


def my_range(start, stop, step=1):
    """
    Nase vlastni implementace range(), chceme, aby se chovala uplne stejne jako range
    """
    results = []
    i = start
    while i < stop:
        results.append(i)
        i += step
    return results

def my_zip(*iterables):
    """
    Nase vlastni implementace zip()

    iterables = [
        ["Alice", "Bob", "Karel", "Eva", "Martin"], -> len() -> 5
        [  30,     20,     24,     18,     27    ],
        [  50,     80,     90,     55,     67    ]
    ]

    results = [
        ('Alice', 30, 50),
        ('Bob',   20, 80),
        ('Karel', 24, 90),
        ('Eva',   18, 55),
        ('Martin',27, 67)
    ]
    """
    results = []
    length = len(iterables[0])  # 5
    i = 0
    while i < length:
        subresult = []
        for iterable in iterables:
            subresult.append(iterable[i])
        results.append(tuple(subresult))
        i += 1
    return results


if __name__ == "__main__":

    jmena = ["Alice", "Bob", "Karel", "Eva", "Martin"]
    vek =   [  30,     20,     24,     18,     27    ]
    vaha =  [  50,     80,     90,     55,     67    ]

    vysledek = list( zip(jmena, vek, vaha) )
    print(vysledek)
    # for jmeno, vek, vaha in vysledek:
    #     print(f'{jmeno} je {vek} let a vazi {vaha} kg')

    vysledek = my_zip(jmena, vek, vaha)
    print(vysledek)


if __name__ == "__main__":
    seznam = list(enumerate(["ahoj", "cau", "jak", "se", "mas"], 2))
    print(seznam)
    seznam = while_enumerate(["ahoj", "cau", "jak", "se", "mas"], 2)
    print(seznam)

    seznam = list(range(1, 10, 2))
    print(seznam)
    seznam = my_range(1, 10)
    print(seznam)
