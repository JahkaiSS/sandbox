import tkinter as tk

def grid(keyword,r=0,c=0):
    return [keyword.grid(row=r,column=c)]


root = tk.Tk()
root.title("Dumbo Wumbo")

def addToList(event=None):
    text = entry.get()
    if len(text) > 0:
        text_list.insert(tk.END, text)
        entry.delete(0,tk.END)


root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

frame = tk.Frame(root)
grid(frame)

entry = tk.Entry(frame)
entry.bind("<Return>",addToList)
grid(entry)

entry_button = tk.Button(frame,text="ADD!",command=addToList)
grid(entry_button,0,1)

text_list = tk.Listbox(frame)
grid(text_list,1,0)
text_list.grid(columnspan=2,sticky="ew")


tk.mainloop()
