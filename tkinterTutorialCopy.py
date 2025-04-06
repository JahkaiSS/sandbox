import tkinter as tk

myReference = {
    "screen = pygame.display.set_mode([w,h])" : 
    "root = tk.Tk()",
    "event loop": "root.mainloop()"}


root = tk.Tk()
rootMethods = [".title()"]
root.title("Simple App")

def click():
    label.config(text="CHICKEN")

widgets = ["tk.Button()", "tk.Label()"]
geometryManagers = [".grid()"]
commonParameters = ["master","text"]
widgetMethods = [(".config()", "to change values")]


label = tk.Label(root, text="Label 1")
label.grid(row=0, column=0)

SEARCH_CHAR = "b"
for i in label.config().keys():
    if i[0] == SEARCH_CHAR:
        print(i)

buttonParameters = ["root","text","command=function"]
btn = tk.Button(root, text="Button 1",command=click)
btn.grid(row=0,column=1)


root.mainloop()
