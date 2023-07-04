##wyswietlnie planszy:
def wyswietl_plansze(plansza):
    for x in range(wielkosc):
        if(x==0):
            print(" ", end=" ")
            for numer_kolumny in range(wielkosc):
                if(numer_kolumny<10):
                    print("0", end="")
                print(numer_kolumny, end=" ") #wyśietlanie numerów kolumny

            print()
        for y in range(wielkosc):
            if(y==0):
                if (x < 10):
                    print("0", end="")
                print(x, end=" ") ##wyswietlanie numerów wierszy
            print(plansza[x][y], end="  ") ##wyświetlanie środka planszy
        print()

def wybieranie_znaku():
    ##gracz wybiera O lub X
    gracz1=input('wybierz X lub O: ')
    if gracz1 == 'X':
        gracz2 = "O"
        print("-------------------------------------")
        print('gracz1 to ' + gracz1 + ' gracz2 to ' + gracz2)
        print("--------------------------------------")

    elif gracz1 == 'O':
        gracz2='X'
        print('gracz1 to ' + gracz1 + ' gracz2 to ' + gracz2)
    else:
        print("podałeś zły znak")
        gracz1, gracz2 = wybieranie_znaku()
    return gracz1, gracz2

##wybranie miejsca przez gracza funkcja

def wybranie_miejsca(gracz, plansza):
    print("gracz z " + gracz + " wybierz pole na którym chcesz postawić pionek: ")
    rzad=int(input('wybierz rząd: '))
    kolumna=int(input('wybierz kolumne: '))

    if (rzad >= wielkosc or kolumna >= wielkosc):
        print("nieprawidłowe dane")
        rzad, kolumna=wybranie_miejsca(gracz, plansza)

    if (plansza[rzad][kolumna] != "?"):
        print("miejsce jest już zajęte")
        rzad, kolumna = wybranie_miejsca(gracz, plansza)

    return rzad, kolumna

##wstawienie do planszy X lub O w miejsce ktore wybral gracz
def wstawienie_do_planszy(rzad, kolumna, gracz, plansza):
    zmieniana_plansza = plansza
    zmieniana_plansza[rzad][kolumna] = gracz
    return zmieniana_plansza

def czy_wygrana(rzad, kolumna, plansza, gracz):
    ile = 0
    #poziom
    for i in range(1,5):
        if(kolumna+i < wielkosc):
            if(plansza[rzad][kolumna+i] == gracz):
                ile = ile + 1
            else:
                break

    for i in range(1,5):
        if(kolumna-i >= 0):
            if(plansza[rzad][kolumna-i] == gracz):
                ile = ile + 1
            else:
                break
    if(ile>=4):
        print("wygrał gracz ze znakiem "+ gracz)
        return True


    ile = 0
    # pion
    for i in range(1, 5):
        if (rzad + i < wielkosc):
            if (plansza[rzad+i][kolumna] == gracz):
                ile = ile + 1
            else:
                break

    for i in range(1, 5):
        if (rzad - i >= 0):
            if (plansza[rzad-i][kolumna] == gracz):
                ile = ile + 1
            else:
                break
    if (ile >= 4):
        print("wygrał gracz ze znakiem " + gracz)
        return True
    ile = 0
        # skos prawy /
    for i in range(1, 5):
        if (rzad + i < wielkosc) and (kolumna - i < wielkosc):
            if (plansza[rzad + i][kolumna - i] == gracz):
                ile = ile + 1
            else:
                break

    for i in range(1, 5):
        if (rzad - i >= 0) and (kolumna + i < wielkosc):
            if (plansza[rzad - i][kolumna + i] == gracz):
                ile = ile + 1
            else:
                break
    if (ile >= 4):
        print("wygrał gracz ze znakiem " + gracz)
        return True

    ile = 0
        # skos lewy \
    for i in range(1, 5):
        if (rzad + i < wielkosc) and (kolumna + i < wielkosc):
            if (plansza[rzad + i][kolumna + i] == gracz):
                ile = ile + 1
            else:
                break

    for i in range(1, 5):
        if (rzad - i >= 0) and (kolumna - i < wielkosc):
            if (plansza[rzad - i][kolumna - i] == gracz):
                ile = ile + 1
            else:
                break
    if (ile >= 4):
        print("wygrał gracz ze znakiem " + gracz)
        return True



def czy_koniec_gry(plansza):
   if any("?" in x for x in plansza):
       return False
   else:
       print("miejsca się skończyły, REMIS")
       return True



wielkosc=int(input('podaj wielkosc planszy: '))
while(wielkosc < 5 or wielkosc > 20):
    print("nieodpowiednia wielkość planszy")
    wielkosc = int(input('podaj jeszcze raz wielkosc planszy: '))

##stworzenie planszy
plansza = [['?' for x in range(wielkosc)] for x in range(wielkosc)]

wyswietl_plansze(plansza)

gracz1, gracz2 = wybieranie_znaku()


while not (czy_koniec_gry(plansza)):

    rzad1, kolumna1 = wybranie_miejsca(gracz1, plansza)
    wstawienie_do_planszy(rzad1, kolumna1, gracz1, plansza)
    wyswietl_plansze(plansza)

    if(czy_wygrana(rzad1, kolumna1, plansza, gracz1)):
        break

    if (czy_koniec_gry(plansza)):
        break

    rzad2, kolumna2=wybranie_miejsca(gracz2, plansza)
    wstawienie_do_planszy(rzad2, kolumna2, gracz2, plansza)
    wyswietl_plansze(plansza)
    if (czy_wygrana(rzad2, kolumna2, plansza, gracz2)):
        break










