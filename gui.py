import tkinter as tk


def build_filemenu(targetbar, root):
    filemenu = tk.Menu(targetbar, tearoff=0)
    filemenu.add_command(label="New")
    filemenu.add_command(label="Open")
    filemenu.add_command(label="Save")
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    return filemenu


def build_helpmenu(targetbar):
    helpmenu = tk.Menu(targetbar, tearoff=0)
    helpmenu.add_command(label="Help Index")
    helpmenu.add_command(label="About...")
    return helpmenu


def build_menubar(root):
    menubar = tk.Menu(root)
    menubar.add_cascade(label="File", menu=build_filemenu(menubar, root))
    menubar.add_cascade(label="Help", menu=build_helpmenu(menubar))
    return menubar


def build_lcol(root):
    frm_buttons = tk.Frame(root, relief=tk.RAISED, bd=2)
    btn_open = tk.Button(frm_buttons, text="Open")
    btn_open.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
    btn_save = tk.Button(frm_buttons, text="Save As...")
    btn_save.grid(row=1, column=0, sticky='ew', padx=5)
    frm_buttons.grid(row=0, column=0, sticky='ns')


def build_rcol(root):
    text_edit = tk.Text(root)
    text_edit.grid(row=0, column=1, sticky='nsew')


def build_gui():
    # Create frame
    root = tk.Tk()
    # Set Title
    root.title("RS3 Dailyscape Log")
    # add Menubar
    root.config(menu=build_menubar(root))
    # Alignment
    root.rowconfigure(0, minsize=800, weight=1)
    root.columnconfigure(1, minsize=800, weight=1)
    # Left Column Buttons
    build_lcol(root)
    # Right Column text field
    build_rcol(root)
    # Display/Run
    root.mainloop()


if __name__ == '__main__':
    build_gui()
