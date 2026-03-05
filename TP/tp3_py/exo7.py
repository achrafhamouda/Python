def amicaux():

    def somme_diviseurs(n):
        s = 0
        k = 1
        while k < n:
            if n % k == 0:
                s += k
            k += 1
        return s

    a = 2
    couples_trouve = 0
    print("Les trois premiers couples de nombres amicaux sont :\n")

    while couples_trouve < 3:
        b = somme_diviseurs(a)
        if b > a and somme_diviseurs(b) == a:
            couples_trouve += 1
            print(f" - Couple {couples_trouve} : ({a}, {b})")
        a += 1

amicaux()

