import tkinter                      # importiert tkinter

def click():
    print("clicked")

root = tkinter.Tk()                 #erstellt das hauptfenster
root.title("Button Test")           #fenstertitel
root.geometry("600x400")            #fenstergröße

#Knöpfe Höhe Breite
button1= tkinter.Button(root, text="Button 1",command=click,width=5 , height=10 )   #erstellt button
button1.grid()                                                 #button1.pack #pack=automatisches anzeigen
                                                                                    #pack und grid dürfen im selben Eltern-Fenster verwendet werden
button2= tkinter.Button(root, text="Button 2",command=click, width=10 , height=5)   #command = sagt diese funktion ausführen
button2.grid()                                                                       #width=Breite in zeichen
                                                                                     #height=Höhe in zeilen
#Knöpfe Navegieren
button3= tkinter.Button(root, text="Button 1",command=click)            #row=Zeile column=spalte
button3.grid(row=0, column=5, padx=30, pady=10)                           #grid =Positionierung im Raster mit meinen befehle
                                                                        #padx/pady Abstand vom rand in x/y richtung (vertikaler Abstand, wirkt nur, wenn Zeilenhöhe groß genug ist)



root.mainloop()                     #startet die schleife