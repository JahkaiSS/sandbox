import tkinter as tk

def quickGrid(keyword,r=0,c=0):
    return [keyword.grid(row=r,column=c)]

def quickSetup(keyword):
    if keyword == "Frame":
        f = tk.Frame(master=root)
        quickGrid(f)
        return f
    if keyword == "Entry":
        e = tk.Entry(frame)
        quickGrid(e)
        return e

root = tk.Tk()
root.title("Dumbo Wumbo")

def addToList(event=None):
    text = entry.get()
    if len(text) > 0:
        text_list.insert(tk.END, text)
        entry.delete(0,tk.END)


frame = quickSetup("Frame")

entry = quickSetup("Entry")
entry.bind("<Return>",addToList)

entry_button = tk.Button(frame,text="ADD!",command=addToList)
quickGrid(entry_button,0,1)

text_list = tk.Listbox(frame)
quickGrid(text_list,1,0)


tk.mainloop()
