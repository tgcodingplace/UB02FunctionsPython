# Definition der Funktionen

def getAnzahlBits(zahl):

    basis = 2

    # getMaxTeiler wurde bereits in Aufgabe 2 besrpochen
    teiler = getMaxTeiler(zahl, basis)
    anzahl = 0

    while teiler > 0:

        # Remember: zahl//teiler kann entweder 1 oder 0 sein
        # --> wir addieren die Anzahl der Einsen auf
        anzahl = anzahl + zahl//teiler
        zahl = zahl%teiler

        teiler = teiler // 2

    return anzahl

def getDualZahl(zahl):

    basis = 2

    teiler = getMaxTeiler(zahl, basis)
    dualzahl = ""

    while teiler > 0:

        dualzahl = dualzahl + str(zahl//teiler)
        zahl = zahl%teiler

        teiler = teiler // 2

    return dualzahl

def getMaxTeiler(zahl, basis):

    teiler = 1

    while teiler < zahl:

        teiler = teiler * basis

    return teiler//basis

# Beginn Hauptprogramm

eingabe = int(input("Eingabe: "))

print("Die duale Darstellung " + getDualZahl(eingabe) + " der Zahl ", end="");
print(str(eingabe) + " besteht aus " + str(getAnzahlBits(eingabe)) + " 1ern")
