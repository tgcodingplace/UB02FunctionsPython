# Definition der Funktionen

# die Function übernimmt die umzudrehende Zahl
def reverse(zahl):

    teiler = 10
    r = 0

    # Prinzip:

    # zahl wäre 54321
    # r ist zu Beginn 0
    # multipliziere r in der Schleife mit 10. r bleibt bei 0.
    # klingt aktuell sinnlos, ist aber im nächsten Durchlauf durchaus sinnvoll.
    # addiere zu r den Divisionsrest aus 54321 % 10 --> macht 1
    # r wird zu 1
    # teile 54321 ganzzahlig wurch 10 --> zahl wird zu 5432
    # nächster Schleifendurchlauf, da zahl noch größer 0 ist
    # multipliziere r mit 10 --> macht 10
    # addiere zu r den Divisionsrest aus 5432 % 10 --> macht 2
    # um so wird r zu 12.
    # teile 5432 ganzzahlig wurch 10 --> zahl wird zu 543
    # # nächster Schleifendurchlauf, da zahl noch größer 0 ist
    # Okay? - spiels für Dich bis zum Ende durch ....

    while zahl > 0:

        r = r * teiler
        r = r + zahl%teiler

        zahl = zahl // 10

    # und ab damit zum Hauptprogramm
    return r

# Beginn des Hauptprogramms

eingabe = int(input("Bitte geben Sie eine Zahl ein: "))

print(str(eingabe) + " <---> " + str(reverse(eingabe)))

