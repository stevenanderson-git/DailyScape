import tkinter as tk

root = tk.Tk()
root.title("RS3 DailyScape Log")

menubar = tk.Menu(root)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index")
helpmenu.add_command(label="About...")
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

root.rowconfigure(0, minsize=800, weight=1)
root.columnconfigure(1, minsize=800, weight=1)



frm_buttons = tk.Frame(root, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons, text="Open")
btn_open.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
btn_save = tk.Button(frm_buttons, text="Save As...")
btn_save.grid(row=1, column=0, sticky='ew', padx=5)
frm_buttons.grid(row=0, column=0, sticky='ns')

#text_edit = tk.Text(root)
#text_edit.grid(row=0, column=1, sticky='nsew')



root.mainloop()