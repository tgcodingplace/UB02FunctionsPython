# Definition der Funktionen

# Ok, übernimm sowohl die Zahl (abgelegt in z)
# als auch die mathematische Basis (abgelegt in b)
# Beispiel:
# z wäre 67, b wäre 2
# multipiziere b wiederholt mit 2 solange der teiler kleiner
# als z ist.
# teiler --> 1 kleiner z --> 67
# multipliziere teiler mit 2
# teiler --> 2 kleiner z --> 67
# multipliziere teiler mit 2
# teiler --> 4 kleiner z --> 67
# multipliziere teiler mit 2
# teiler --> 8 kleiner z --> 67
# multipliziere teiler mit 2
# teiler --> 16 kleiner z --> 67
# multipliziere teiler mit 2
# teiler --> 32 kleier z --> 67
# multipliziere teiler mit 2
# teiler --> 64 kleiner z --> 67
# multipliziere teiler mit 2
# teiler --> 128 NICHT MEHR kleiner z --> 67
# Abbruch der Schleife
# sende teiler//2 (--> 64) als größten Teiler
# an den Aufrufer zurück ...
# Okay?
# funktioniert mit 16 (hexadezimal genauso ...)

def getMaxTeiler(z, b):

    teiler = 1

    while teiler < z:

        teiler = teiler * b

    return teiler//b

# Beginn Hauptprogramm

eingabe = int(input("Eingabe der Zahl : "))
basis   = int(input("Eingabe der Basis: "))

print("Der größte Teiler zur Basis " + str(basis), end=" ")
print("lautet für die Zahl " + str(eingabe), end=" ")
print(getMaxTeiler(eingabe, basis))

eingabe = int(input("Eingabe der Zahl : "))
basis   = int(input("Eingabe der Basis: "))

print("Der größte Teiler zur Basis " + str(basis), end=" ")
print("lautet für die Zahl " + str(eingabe), end=" ")
print(getMaxTeiler(eingabe, basis))
