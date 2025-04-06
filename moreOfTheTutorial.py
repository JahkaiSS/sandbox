import tkinter as tk

def quickGrid(keyword,r=0,c=0):
    return keyword.grid(row=r,column=c)

root = tk.Tk()
root.title("Dumbo Wumbo")

def addToList(event=None):
    text = entry.get()
    if len(text) > 0:
        text_list.insert(tk.END, text)
        entry.delete(0,tk.END)

def clearList():
    text_list.delete(0, tk.END)



frame = tk.Frame(root)
quickGrid(frame)

entry = tk.Entry(frame)
quickGrid(entry)
entry.bind("<Return>",addToList)

entry_button = tk.Button(frame,text="ADD!",command=addToList)
quickGrid(entry_button,0,1)

delete_button = tk.Button(frame,text="DEL!",command=clearList)
quickGrid(delete_button,1,1)

text_list = tk.Listbox(frame)
quickGrid(text_list,1,0)


tk.mainloop()
