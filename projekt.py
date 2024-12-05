historia_wynikow = []

def dodaj_do_historii(opis, wynik):
    historia_wynikow.append(f"{opis}: {wynik}")

def wyswietl_historie():
    print("\n HISTORIA KONWERSJI")
    if not historia_wynikow:
        print("Brak wyników do wyświetlenia.")
    else:
        for i, wpis in enumerate(historia_wynikow, 1):
            print(f"{i}. {wpis}")

def menu_glowne():
    print("\n KONWERTER JEDNOSTEK")
    print("1. Długość")
    print("2. Masa")
    print("3. Temperatura")
    print("4. Historia wyników")
    print("5. Wyjście")
    return input("Wybierz kategorię (1-5): ")

def konwerter_dlugosci():
    while True:
        print("\n KONWERTER DŁUGOŚCI")
        print("1. Metry na kilometry")
        print("2. Kilometry na mile")
        print("3. Mile na kilometry")
        print("4. Centymetry na cale")
        print("5. Powrót")
        wybor = input("Wybierz konwersję (1-5): ")
        
        if wybor == "1":
            metry = float(input("Podaj liczbę metrów: "))
            wynik = metry / 1000
            print(f"{metry} metrów to {wynik} kilometrów.")
            dodaj_do_historii(f"{metry} metrów na kilometry", wynik)
        elif wybor == "2":
            km = float(input("Podaj liczbę kilometrów: "))
            wynik = km * 0.621371
            print(f"{km} kilometrów to {wynik} mil.")
            dodaj_do_historii(f"{km} kilometrów na mile", wynik)
        elif wybor == "3":
            mile = float(input("Podaj liczbę mil: "))
            wynik = mile / 0.621371
            print(f"{mile} mil to {wynik} kilometrów.")
            dodaj_do_historii(f"{mile} mil na kilometry", wynik)
        elif wybor == "4":
            cm = float(input("Podaj liczbę centymetrów: "))
            wynik = cm / 2.54
            print(f"{cm} centymetrów to {wynik} cali.")
            dodaj_do_historii(f"{cm} centymetrów na cale", wynik)
        elif wybor == "5":
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

def konwerter_masy():
    while True:
        print("\n KONWERTER MASY")
        print("1. Kilogramy na funty")
        print("2. Funty na kilogramy")
        print("3. Gramy na kilogramy")
        print("4. Kilogramy na uncje")
        print("5. Powrót")
        wybor = input("Wybierz konwersję (1-5): ")
        
        if wybor == "1":
            kg = float(input("Podaj liczbę kilogramów: "))
            wynik = kg * 2.20462
            print(f"{kg} kilogramów to {wynik} funtów.")
            dodaj_do_historii(f"{kg} kilogramów na funty", wynik)
        elif wybor == "2":
            funty = float(input("Podaj liczbę funtów: "))
            wynik = funty / 2.20462
            print(f"{funty} funtów to {wynik} kilogramów.")
            dodaj_do_historii(f"{funty} funtów na kilogramy", wynik)
        elif wybor == "3":
            gramy = float(input("Podaj liczbę gramów: "))
            wynik = gramy / 1000
            print(f"{gramy} gramów to {wynik} kilogramów.")
            dodaj_do_historii(f"{gramy} gramów na kilogramy", wynik)
        elif wybor == "4":
            kg = float(input("Podaj liczbę kilogramów: "))
            wynik = kg * 35.274
            print(f"{kg} kilogramów to {wynik} uncji.")
            dodaj_do_historii(f"{kg} kilogramów na uncje", wynik)
        elif wybor == "5":
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

def konwerter_temperatury():
    while True:
        print("\n KONWERTER TEMPERATURY")
        print("1. Celsius na Fahrenheit")
        print("2. Fahrenheit na Celsius")
        print("3. Celsius na Kelvin")
        print("4. Kelvin na Celsius")
        print("5. Powrót")
        wybor = input("Wybierz konwersję (1-5): ")
        
        if wybor == "1":
            celsius = float(input("Podaj temperaturę w Celsius: "))
            wynik = celsius * 9/5 + 32
            print(f"{celsius}°C to {wynik}°F.")
            dodaj_do_historii(f"{celsius}°C na Fahrenheit", wynik)
        elif wybor == "2":
            fahrenheit = float(input("Podaj temperaturę w Fahrenheit: "))
            wynik = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F to {wynik}°C.")
            dodaj_do_historii(f"{fahrenheit}°F na Celsius", wynik)
        elif wybor == "3":
            celsius = float(input("Podaj temperaturę w Celsius: "))
            wynik = celsius + 273.15
            print(f"{celsius}°C to {wynik} K.")
            dodaj_do_historii(f"{celsius}°C na Kelvin", wynik)
        elif wybor == "4":
            kelvin = float(input("Podaj temperaturę w Kelvin: "))
            wynik = kelvin - 273.15
            print(f"{kelvin} K to {wynik}°C.")
            dodaj_do_historii(f"{kelvin} K na Celsius", wynik)
        elif wybor == "5":
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

def main():
    while True:
        wybor = menu_glowne()
        if wybor == "1":
            konwerter_dlugosci()
        elif wybor == "2":
            konwerter_masy()
        elif wybor == "3":
            konwerter_temperatury()
        elif wybor == "4":
            wyswietl_historie()
        elif wybor == "5":
            print("Dziękujemy za skorzystanie z konwertera!")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()
