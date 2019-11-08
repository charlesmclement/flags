import Tkinter
import os

tk = Tkinter.Tk()
tk.title("flags")
tk.geometry("300x100")
tk.resizable(False, False)

d = {}
with open("flags.txt") as f:
    for line in f:
        if len(line) is not 1:
            try:
                (key, val) = line.split(',')
                d[key] = val.rstrip()
            except:
                print("Warning: Max of two columns, lines removed")

def dropdown(active_value):
    global active
    active = d[active_value]
    button_drop["state"] = "normal"
    button_del["state"] = "normal"
    button_drop.config(text = "Drop {} flag".format(active))
    button_del.config(text = "Delete {} flag".format(active))


def dropflag():
    try:
        open(active, 'a').close()
    except NameError:
        print("Select an option")

def delflag():
    try:
        os.remove(active)
    except NameError:
        print("Select an option")
    except WindowsError:
        print("File not found")
        
var = Tkinter.StringVar()
var.set('Version')

p = Tkinter.OptionMenu(tk, var, *d, command=dropdown)
p.pack()
button_drop = Tkinter.Button(command=dropflag)
button_del= Tkinter.Button(command=delflag)
button_drop["state"] = "disabled"
button_del["state"] = "disabled"
button_drop.pack()
button_del.pack()

tk.mainloop()