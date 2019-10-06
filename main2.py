def merge(dane1, dane2):
    rozmiar = len(dane1) + len(dane2) -1
    max = len(dane1) - 1
    p = 0
    q = 0
    wynik = []

    for i in range(0, rozmiar):
        if p == max:
            wynik.append(dane2[q])
            q += 1
        elif q == max:
            wynik.append(dane1[p])
            p += 1
        elif dane1[p] < dane2[q]:
            wynik.append(dane1[p])
            p += 1
        else:
            wynik.append(dane2[q])
            q += 1

    return wynik