import func, books


while True:
    print("_+_+_"*40)
    print("i - informcja ogulna o bibliotece\n"
          "edb - edycja biblioteki\n"
          "edk - edycja ksianzki\n"
          "cr - tworzenie ksianzki\n"
          "fb - znalezc ksianzke\n"
          "ex - koniec dzialania")
    inp = input("Działanie: ").lower()
    if inp == "i":
        func.inf_library(books.library)
    elif inp == "edb":
        func.edit_library(books.library)
    elif inp == "edk":
        x = input("Biblioteka - b\n"
                  "magazyn -- m\n"
                  "odp: ").lower()
        if x == "b":
            func.edit_book(books.library)
        elif x == "m":
            func.edit_book(books.mg)
    elif inp == "cr":
        books.create_book()
    elif inp == "fb":
        x = func.finder(books.library)
        print(f"Twoja ksienzka")
        func.inf_book(x)
    elif inp == "ex":
        print("Program zakończy działanie")
        break
    else:
        print("Nie ma takiej komendy")