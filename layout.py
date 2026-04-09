import tkinter

def click_text():
    print(entry.get())                   #text aus Entry feld holen

def clear_text():
    entry.delete(0, tkinter.END)       #Eingabefeld leeren von anfang bis ende

root = tkinter.Tk()
root.geometry("500x400")
root.title("GUI Layout Übung")

# Frame
main_frame = tkinter.Frame(root)
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# ??? Knopf (oben)
button4 = tkinter.Button(main_frame, text="???", command=click_text)
button4.grid(row=0, column=0, columnspan=3, pady=5)

# Eingabefeld darunter
entry = tkinter.Entry(main_frame, width=20)
entry.grid(row=1, column=0, columnspan=3, pady=5)

#knöpfe rechts nebeneinander
button1 = tkinter.Button(main_frame, text="Button 1", command=lambda: entry.insert(0,"1"))
button2 = tkinter.Button(main_frame, text="Button 2", command=lambda: entry.insert(0,"2"))
button3 = tkinter.Button(main_frame, text="Button 3", command=lambda: entry.insert(0,"3"))

button1.grid(row=1, column=5, padx=5, pady=5)
button2.grid(row=1, column=6, padx=5, pady=5)
button3.grid(row=1, column=7, padx=5, pady=5)

# Leeren knopf unten
button5 = tkinter.Button(main_frame, text="Leeren", command=clear_text)
button5.grid(row=3, column=0, columnspan=3, pady=10)


  ##frames= für struktur um sachen zu gruppieren
  ##top für Eingabe ausgabe
#top_frame = tkinter.Frame(root)
#top_frame.grid(row=0, column=0, pady=10)                             #muss nur gestapelt gestapelt werden postition egal
  ##mid für oben
#middle_frame = tkinter.Frame(root)
#middle_frame.grid(row=1, column=0, pady=10)                          #abstand ziwschen frames
  ##bot für unten
#bottom_frame = tkinter.Frame(root)
#bottom_frame.grid(row=2, column=0, pady=10)

  ##Eingabe und Ausgabe
#entry = tkinter.Entry(top_frame, width=20)                      #position top
#entry.grid(row=1, column=0, padx=5)                             #grid weil position ordentlich machen per befehl


  ##Buttons oben
#button1 = tkinter.Button(middle_frame, text="Button 1", command=lambda: entry.insert(0,"1"))    #insert fügt text in eintry feld ein
#button2 = tkinter.Button(middle_frame, text="Button 2", command=lambda: entry.insert(0,"2"))    #lambda= ein platzhalter da command eine funktion erwartet
#button3 = tkinter.Button(middle_frame, text="Button 3", command=lambda: entry.insert(0,"3"))    #mit lambda kan ich direkt sagen was dahinter passieren soll ohne funktion

#button1.grid(row=0, column=0, padx=5, pady=5)                       #row =Zeile
#button2.grid(row=0, column=1, padx=5, pady=5)                       #column=spaöte
#button3.grid(row=0, column=2, padx=5, pady=5)                       #padx/y = Abstand in x/y-Richtung also horizontal/vertikal
#button1.place(relx=0,rely=1.5)
  ##Buttons daneben/darunter
#button4 = tkinter.Button(bottom_frame, text="???", command=click_text)
#button5 = tkinter.Button(bottom_frame, text="Leeren", command=clear_text)

#button4.grid(row=0, column=0, padx=5, pady=5)
#button5.grid(row=0, column=1, padx=5, pady=5)

root.mainloop()
