import uuid

library = [{
    "Name": "Fizik",
    "Quantity": "50",
    "style": "school",
    'id': str(uuid.uuid4())
}, {
    "Name": "Lord of the rings",
    "Quantity": "75",
    "style": "fantasy",
    'id': str(uuid.uuid4())
},{
    "Name": "The Hobbit or There and Back Again",
    "Quantity": "30",
    "style": "fantasy",
    'id': str(uuid.uuid4())
},{
    "Name": "Trawel for power",
    "Quantity": "30",
    "style": "fantasy",
    'id': str(uuid.uuid4())
}, {
    "Name": "H",
    "Quantity": "21",
    "style": "horror",
    'id': str(uuid.uuid4())
}]
# ---------------------------------
mg = [{
    "Name": "Bicentennial Man",
    "Quantity": "8",
    "style": "si-fy",
    'id': str(uuid.uuid4())
}, {
    "Name": "Bible",
    "Quantity": "90",
    "style": "fantasy",
    'id': str(uuid.uuid4())
}]


def create_book() -> None:
    book = {
        "Name": "",
        "Quantity": "",
        "style": "",
        'id': str(uuid.uuid4())
    }
    x = input("Wprowadz Name: ")
    book["Name"] = x
    while True:
        try:
            x = input("Wprowadz Quantity: ")
            x = int(x)
            book["Quantity"] = str(x)
            break
        except ValueError:
            print("to nie jest liczba")
    while True:
        x = input("Wybierz styl:\n"
                  "f - fantasy\n"
                  "sf - si-fy\n"
                  "h - horror\n"
                  "sc - school\n"
                  "Odp: ").lower()
        if x == "f" or x == "fantasy" or x == "1":
            book["style"] = "fantasy"
            break
        elif x == "sf" or x == "si-fy" or x == "2":
            book["style"] = "si-fy"
            break
        elif x == "h" or x == "horror" or x == "3":
            book["style"] = "horror"
            break
        elif x == "sc" or x == "school" or x == "4":
            book["style"] = "school"
            break
        else:
            print("Nie ma takiej opcji")
    print("Stworzylesz:")
    for k, v in book.items():
        print(f"{k}:  {v}")
    mg.append(book)
    print("Znajdziesz w magazynie")
    print("*" + "-" * 40 + "*" + "\n\n")
