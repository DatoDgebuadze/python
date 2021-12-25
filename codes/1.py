from cryptography.fernet import Fernet

paroli = input("Ra aris sheni mtavari paroli? ")


def naxva():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            x, y = data.split("|")
            print("User:", x, "| Password:", y)


def damateba():
    saxeli = input('Momxmareblis Saxeli: ')
    paroli = input('paroli: ')

    # main mods are w a- creates entirly new one evry turn ,r is read mode, a is append mode most flexible mode it allows to add, create new if needed.
    with open('passwords.txt', 'a') as f:
        f.write(saxeli + "\n" + paroli + "\n")


while True:
    archevani = input(
        "Gsurs Axali Parolis Damateba Tu qsurs arsebulis naxva(naxva, damateba, daachire q rom gamorto: ")
    if archevani == "q":
        break
    if archevani == "naxva":
        naxva()
    if archevani == "damateba":
        damateba()
    else:
        print("Shecdoma mogivida")
