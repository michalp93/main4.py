# Przykład prostej funckji
def simple_function():
    print('Hello world!')
    print('Wikipedia')


simple_function()

# Instrukcja return
def myfunction():
    return 3+3


print(myfunction())

# Argumenty
def add(x, y):
    return x + y


print(add(2, 3))

# Docstring
def my_function():
    """Dokumentacja funkcji"""


help(my_function)

# Rekurencja/rekursja (ang. recursion) tzn. Powtarza samą siebie

# Cwiczenie 1 o rozmanażaniu się królików, inaczej ciąg Fibbonaciego
def fibbonaci_numbers(n):
    ''' zwraca liczby Fibonacciego mniejsze od n '''
    wynik = []
    a, b = 0, 1
    while a < n:
    # while len(wynik) < n:
        wynik.append(a)
        a, b = b, a + b
    return wynik


x = fibbonaci_numbers(10)
print(x)
print(fibbonaci_numbers.__doc__)

# Cwiczenie 2
# Napisz funkcję w Pythonie do obliczania długości łańcucha.
# Bez uzywania funkcji len
def dlugosc_lancucha(n):
    m = 0

    for num in n:
        m += 1
    return m


print(dlugosc_lancucha("Alabama"))

# Cwiczenie 3
# Napisz funkcję w Pythonie, która zsumuje wszystkie elementy na liście.
def suma_elementow(n):
    suma_el = 0

    for num in n:
         suma_el += num
    return suma_el


print(suma_elementow([1, 2, 3, 4, 5]))

# Cwiczenie 4
# Napisz funkcję w Pythonie, który mnoży wszystkie elementy na liście.
# def mnozenie_elementow(lista):
#     wynik = 1
#
#     for element in lista:
#          wynik *= element
#     return wynik
#
#
# print(mnozenie_elementow([1, 2, 3, 4, 5]))

# To samo tylko inaczej, bardziej zoptymalizowane
def mnozenie_elementow(lista):
    wynik = lista[0]

    for element in lista[1:]:
         wynik *= element
    return wynik


print(mnozenie_elementow([1, 2, 3, 4, 5]))

# Cwiczenie 5
# Napisz funkcję w Pythonie, aby uzyskać największą liczbę z listy.
def najwieksza_liczba(lista):
    wartosc = lista[0]
    for element in lista[1:]:
        if element > wartosc:
            wartosc = element
    return wartosc

print(najwieksza_liczba([10, 50, 111, -3, 131, 1]))

# Cwiczenie 6
# Napisz funkcję w Pythonie, który zlicza liczbę znaków (częstotliwość znaków) w ciągu.
# Przykładowy ciąg : google.com
# Oczekiwany wynik : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
def liczba_znakow(ciag):
    wartosc = {}

    for znak in ciag:
        klucze = wartosc.keys()
        #print(wartosc)
        if znak in klucze:
            wartosc[znak] += 1
        else:
            wartosc[znak] = 1
    return wartosc


print(liczba_znakow("google.com"))

# Cwiczenie 7
# Napisz funkcję w Pythonie, który zlicza ciągi znaków, w których długość ciągu wynosi 2 lub więcej, a pierwszy i ostatni znak są takie same z podanej listy ciągów.
# Przykładowa lista : ['abc', 'xyz', 'aba', '1221']
# Oczekiwany wynik: 2
def liczba_ciagow(x):
    a = 0
    for n in x:
        if len(n) >= 2 and n[0] == n[-1]:
            a += 1
    return a

print(liczba_ciagow(['abc', 'xyz', 'aba', '1221']))

# Cwiczenie 8
# Napisz funkcję w Pythonie, aby uzyskać listę posortowaną w porządku rosnącym
# według ostatniego elementu w każdej krotce z podanej listy niepustych krotek.
# Przykładowa lista: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Oczekiwany wynik : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
lista = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def drugi_element(krotka):
    return krotka[-1]

def sortuj(lista):
    return sorted(lista, key=drugi_element)


print(sortuj(lista))

# Cwiczenie 9
# Napisz funkcję w Pythonie, aby uzyskać łańcuch składający się z pierwszych 2 i ostatnich 2 znaków z danego łańcucha. Jeśli długość ciągu jest mniejsza niż 2, zwróć zamiast tego pusty ciąg.
# Przykładowy ciąg : Python
# Oczekiwany wynik: Pyon
# Przykładowy ciąg : Py
# Oczekiwany wynik: PyPy
# Przykładowy ciąg : P
# Oczekiwany wynik: pusty ciąg
def string_con(x):

    if len(x) < 2:
        return ""
    else:
        return x[:2] + x[-2:]


print(string_con("Python"))

# Inaczej, krócej bez else:

def string_con(x):

    if len(x) < 2:
        return ""
    return x[:2] + x[-2:]


print(string_con("Python"))

# Cwiczenie 10
# Napisz program, policzy silnię dla liczby n tj.
# n! = 1*2*3*4...*(n-2)*(n-1)*n
# Zrób to przez napisanie funkcji, która rekurencyjne będzie się odwoływała do samej siebie
# do momentu gdy będzie liczyła silnie dla 1, która wynosi 1.
def silnia(n):
    if n > 1:
        return silnia(n - 1) * n
    else:
        return 1

print(silnia(5))

# Cwiczenie 11
# Rekurencyjny ciąg Fibonacciego
def re_fibonacci(n):
    if n >= 2:
        return re_fibonacci(n - 1) + re_fibonacci(n - 2)
    else:
        return n

print(re_fibonacci(5))