import tkinter

root = tkinter.Tk()
root.title("Button Test")
root.geometry("400x300")

button1= tkinter.Button(root, text="Button 1")
button1.pack()

button2= tkinter.Button(root, text="Button 2")
button2.pack()

root.mainloop()