import tkinter                      # importiert tkinter

def click():
    print("clicked")

root = tkinter.Tk()                 #erstellt das hauptfenster
root.title("Button Test")           #fenstertitel
root.geometry("400x300")            #fenstergröße

button1= tkinter.Button(root, text="Button 1",command=click,width=20 , height=3 )   #erstellt button
button1.pack()                                                                      #zeigt den button an

button2= tkinter.Button(root, text="Button 2",command=click, width=10 , height=20)   #command = sagt diese funktion ausführen
button2.pack()                                                                       #width=Breite in zeichen
                                                                                     #height=Höhe in zeilen

root.mainloop()                     #startet die schleife