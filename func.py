import books


def inf_book(dc: dict) -> None:
    for k, v in dc.items():
        print(f"{k}:  {v}")


def inf_library(lst: list) -> None:
    for dic in lst:
        inf_book(dic)
        print("---" * 10)


def finder(lis: list) -> dict:
    inf_library(lis)
    while True:
        l = []
        print("*" * 60)
        inp = input("ex - wyjsc\n"
                    "Wprowadz nazwe lub styl lub id: ")
        if inp == "ex":
            break
        else:
            for el in lis:
                for k, v in el.items():
                    if v.lower() == inp.lower():
                        l.append(el)
            if len(l) == 1:
                return l[0]
            elif len(l) > 1:
                inf_library(l)
                print("szukaj dalej")
            else:
                print("nic nie znaleziono")
# ----------------------------------------


def edit_book(lis: list) -> None:
    while True:
        print("Jakiej ksianzce edycje robisz?")
        book = finder(lis)
        if book is None:
            break
        else:
            for i in range(len(lis)):
                if book == lis[i]:
                    break
            inf_book(book)
            x = "id"
            while x == "id":
                x = input("Co chcesz edukowac?\n"
                          "Odp: ").lower()
                if x == "id":
                    print("id nie mozna edukowac")

            for k, v in book.items():
                if k.lower() == x:
                    y = input("Nowe dane: ")
                    book[k] = y
                    break
            lis[i] = book


def book_to_l(a: str, l1: list, l2: list) -> None:
    y = ""
    while y != 'y':
        d = finder(l2)
        if d is None:
            y = input("Chcesz wyjsc?\n"
                      "y -- tak\n"
                      "n -- nie\n"
                      "Odp: ").lower()
        else:
            print(f"Chcesz {a}:")
            inf_book(d)
            y = input("y -- tak\n"
                      "n -- nie\n"
                      "Odp: ").lower()
            if y == 'y':
                l1.append(d)
                l2.remove(d)


# ----------------------------------------


def edit_library(lst: list) -> None:
    while True:
        inf_library(lst)
        print("*" * 50)
        print("Magazyn: ")
        inf_library(books.mg)
        x = input("Opcje:\n"
                  "d - dodac ksianzke do biblioteki\n"
                  "u -- usunanc\n"
                  "ex -- wyjsc\n"
                  "Odp: ").lower()
        if x == "d":
            book_to_l("dodac", books.library, books.mg)
        elif x == "u":
            book_to_l("usunanc", books.mg, books.library)
        elif x == "ex":
            break
        else:
            print("niema takiej komendy")

