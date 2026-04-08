import tkinter                      # importiert tkinter

def click():
    print("clicked")

root = tkinter.Tk()                 #erstellt das hauptfenster
root.title("Button Test")           #fenstertitel
root.geometry("400x300")            #fenstergröße

button1= tkinter.Button(root, text="Button 1",command=click)   #erstellt button
button1.pack()                                                  #zeigt den button an

button2= tkinter.Button(root, text="Button 2",command=click)   #command = sagt diese funktion ausführen
button2.pack()

root.mainloop()                     #startet die schleife