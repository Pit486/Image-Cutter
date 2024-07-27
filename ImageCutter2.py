from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image
n = 0

def cutter():
    f = filedialog.askopenfilename() #запрос открытия файла
    global n, xf, yf, xs, ys, column, line
    x = xs-xf
    y = ys-yf
    k = 0
    kol = Image.open(f)
    p = line*column
    for i in range(p):
        k=k+1
        if k==line+1:
            y=y+yf
            x = xs-xf
            k = 1
        n=n+1
        card = kol.crop((x+xf,y+yf,x+xf+xf,y+yf+yf))
        card.save(f_name + str(n)+'.png')
        x=x+xf
        label["text"] = 'Ok!'
    return 

def button_press_2():
    c.delete("all")
    global x
    x=(int(entry.get()))
    domik(x,col)

tk = Tk()
tk.title("Image Cutter v.2.0")
tk.geometry("400x500")
label = ttk.Label()
label.configure(foreground="orange", background="green", width=4, anchor="center", font=("Arial Narrow", 30)) 
label.pack(side=BOTTOM, anchor=S, padx=6, pady=6)

labelxf = ttk.Label()
labelxf.pack(anchor=NW, padx=2, pady=0)
labelxf["text"] = 'Output image width'
entryxf = ttk.Entry()
entryxf.pack(anchor=NW, padx=6, pady=6)
entryxf.insert(0, "540")

labelyf = ttk.Label()
labelyf.pack(anchor=NW, padx=2, pady=0)
labelyf["text"] = 'Output image height'
entryyf = ttk.Entry()
entryyf.pack(anchor=NW, padx=6, pady=6)
entryyf.insert(0, "745")

labelxs = ttk.Label()
labelxs.pack(anchor=NW, padx=2, pady=0)
labelxs["text"] = 'Start position X'
entryxs = ttk.Entry()
entryxs.pack(anchor=NW, padx=6, pady=6)
entryxs.insert(0, "86")

labelys = ttk.Label()
labelys.pack(anchor=NW, padx=2, pady=0)
labelys["text"] = 'Start position Y'
entryys = ttk.Entry()
entryys.pack(anchor=NW, padx=6, pady=6)
entryys.insert(0, "107")

label_l = ttk.Label()
label_l.pack(anchor=NW, padx=2, pady=0)
label_l["text"] = 'Number of lines'
entry_l = ttk.Entry()
entry_l.pack(anchor=NW, padx=6, pady=6)
entry_l.insert(0, "3")

label_c = ttk.Label()
label_c.pack(anchor=NW, padx=2, pady=0)
label_c["text"] = 'Number of columns'
entry_c = ttk.Entry()
entry_c.pack(anchor=NW, padx=6, pady=6)
entry_c.insert(0, "3")

label_f = ttk.Label()
label_f.pack(anchor=NW, padx=2, pady=0)
label_f["text"] = 'Output filename'
entry_f = ttk.Entry()
entry_f.pack(anchor=NW, padx=6, pady=6)
entry_f.insert(0, "example")

xf = int(entryxf.get())
yf = int(entryyf.get())
xs = int(entryxs.get())
ys = int(entryys.get())
line = int(entry_l.get())
column = int(entry_c.get())
f_name = str(entry_f.get())
print(type(f_name))


display_button = ttk.Button(text="Cut", command=cutter)
display_button.pack(side=BOTTOM, anchor=N, padx=6, pady=6)
 


mainloop()

