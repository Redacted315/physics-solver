import tkinter as tk

master = tk.Tk()


label_column = tk.Frame(master)
entry_column = tk.Frame(master)

vl = tk.Label(label_column,text="Velocity:")
ml = tk.Label(label_column,text="Mass:")
al = tk.Label(label_column,text="Acceleration:")
dl = tk.Label(label_column,text="Distance:")
tl = tk.Label(label_column,text="Time:")
momentuml = tk.Label(label_column,text="Momentum:")
vl.pack(side=tk.TOP,anchor=tk.NW)
ml.pack(side=tk.TOP,anchor=tk.NW)
al.pack(side=tk.TOP,anchor=tk.NW,pady=2)
dl.pack(side=tk.TOP,anchor=tk.NW)
tl.pack(side=tk.TOP,anchor=tk.NW)
momentuml.pack(side=tk.TOP,anchor=tk.NW,pady=2)


ve = tk.Entry(entry_column, width=8)
ml = tk.Entry(entry_column, width=8)
al = tk.Entry(entry_column, width=8)
dl = tk.Entry(entry_column, width=8)
tl = tk.Entry(entry_column, width=8)
momentuml = tk.Entry(entry_column, width=8)
entry_list = [ve,ml,al,dl,tl,momentuml]
ve.pack(side=tk.TOP,anchor=tk.NW,pady=2)
ml.pack(side=tk.TOP,anchor=tk.NW,pady=2)
al.pack(side=tk.TOP,anchor=tk.NW,pady=2)
dl.pack(side=tk.TOP,anchor=tk.NW,pady=2)
tl.pack(side=tk.TOP,anchor=tk.NW,pady=2)
momentuml.pack(side=tk.TOP,anchor=tk.NW,pady=2)


def button_go():
    for i in entry_list:
        print(i)# print(i.get())

go_button = tk.Button(master,text="GO",command=button_go)

go_button.pack(side=tk.BOTTOM)


label_column.pack(side=tk.LEFT)
entry_column.pack(side=tk.RIGHT)


master.resizable("false", "false")

master.mainloop()