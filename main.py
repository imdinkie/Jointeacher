import csv
import webbrowser
import pyperclip
import msvcrt
import os
import sys


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def GetTeacherShort():
    teacher_short = input("Lehrerkürzel eingeben:\n").capitalize()
    return teacher_short


def ChangeUmlauts(teacher_short):
    umlautDict = {
        "ä": "ae",
        "ö": "oe",
        "ü": "ue",
    }
    for i, j in umlautDict.items():
        teacher_short = teacher_short.replace(i, j)
    return teacher_short


def GoToWebsite():
    teacher_short = ChangeUmlauts(GetTeacherShort())

    if teacher_short in roomnumberdict:
        webbrowser.open("https://gymnasiumspaichingen.webex.com/meet/" + teacher_short)
        raumnummer = roomnumberdict.get(teacher_short).split(";")
    else:
        print('Dieses Lehrerkürzel existiert nicht im Datenblatt.')
        os.system("pause")
        return
    print('Raum von "' + raumnummer[1] + '" wurde im Browser geöffnet!')
    os.system("pause")


def CopyRoomnumber():
    teacher_short = ChangeUmlauts(GetTeacherShort())

    if teacher_short in roomnumberdict:
        raumnummer = roomnumberdict.get(teacher_short).split(";")
    else:
        print("Dieses Lehrerkürzel existiert nicht im Datenblatt.")
        os.system("pause")
        return

    pyperclip.copy(raumnummer[0])
    print('Raumnummer von "' + raumnummer[1] + '" wurde in die Zwischenablage kopiert!')
    os.system("pause")


clear = lambda: os.system('cls')

with open(resource_path("raumnummern.csv"), encoding='iso-8859-1', mode='r') as inp:
    reader = csv.reader(inp)
    roomnumberdict = {rows[0]: rows[1] for rows in reader}

# Actually starts here

while True:
    clear()
    print(
        "L eingeben, um den Lehrerlink direkt aufzurufen.\nR eingeben, um die Raumnummer in die Zwischenablage zu kopieren.")
    start_options = msvcrt.getch().decode('ASCII')

    if start_options.upper() == 'L':
        clear()
        GoToWebsite()
    elif start_options.upper() == 'R':
        clear()
        CopyRoomnumber()
    else:
        print("Entweder L oder R eingeben.")
        os.system("pause")
