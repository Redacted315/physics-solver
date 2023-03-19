import tkinter as tk
from time import sleep
from tkinter import messagebox
from physics import Physics
import webbrowser

master = tk.Tk()
comp = Physics()

master.title("Variable Detective")
master.resizable(False, False)
master.iconbitmap("assets/icon.ico")
master.option_add('*tearOff', False)
stat_font = ("Arial", 20)


def callback(url):
    webbrowser.open_new_tab(url)


def link_github():
    github = tk.Toplevel(master)
    github.geometry("300x70")
    link = tk.Label(github, text='Contribute on GitHub!', font='Arial 12 underline', fg='blue')
    link.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    link.bind("<Button-1>", lambda e: callback("https://github.com/Redacted315/physics-solver"))


menu_bar = tk.Menu(master)
master['menu'] = menu_bar
menu_options = tk.Menu(menu_bar)
menu_edit = tk.Menu(menu_bar)
menu_bar.add_cascade(menu=menu_options, label='Options')
menu_bar.add_cascade(menu=menu_edit, label='Help')
menu_options.add_command(label='Coming soon...', state='disabled', activebackground='SystemMenu')
menu_options.add_command(label='Close', command=quit)
menu_edit.add_command(label='Help', command=link_github)

label_column_one = tk.Frame(master)
entry_column_one = tk.Frame(master)
label_column_two = tk.Frame(master)
entry_column_two = tk.Frame(master)
label_column_three = tk.Frame(master)
entry_column_three = tk.Frame(master)
button_frame = tk.Frame(master)

delta = '\u0394'
entry_list = []
for i in list(comp.variableDict.keys()):
    label_frame = label_column_one
    entry_frame = entry_column_one
    # print(list(comp.variableDict.keys()).index(i))
    if list(comp.variableDict.keys()).index(i) >= 10:
        label_frame = label_column_two
        entry_frame = entry_column_two
    tk.Label(label_frame, text=i.replace("_", " ").replace("change", delta),
             font=stat_font).pack(side=tk.TOP, anchor='e', pady=1)
    a = tk.Entry(entry_frame, width=8, name=i, font=stat_font)
    entry_list.append(a)

for entry in entry_list:
    entry.pack(side=tk.TOP, anchor=tk.NW, pady=2)


def warning_background():  # flashes entry background colour
    for entry in entry_list:
        entry.configure(state='disabled', disabledbackground='#ebd36c')  # yellow
    master.update_idletasks()
    sleep(0.2)
    for entry in entry_list:
        entry.configure(state='disabled', disabledbackground='#bf6e60')  # red
    master.update_idletasks()
    sleep(0.2)
    for entry in entry_list:
        entry.configure(state='normal')


def blink_warning():
    import winsound
    winsound.PlaySound('SystemHand', winsound.SND_ASYNC)
    # .SND_ASYNC returns immediately, without this none of the following code will execute until
    # the sound has finished playing in its entirety
    for i in range(3):
        warning_background()


def reset_entrys():
    for entry in entry_list:
        entry.configure(background='SystemWindow', state='normal')
        entry.delete(0, tk.END)
        master.focus()  # remove cursor focus from entry's


def is_valid(value):
    try:
        float(value)
        return True
    except TypeError and ValueError:
        return False


# noinspection PyBroadException
def submit_variables():
    values_list = []
    for entry in entry_list:
        value = entry.get()
        if value == '':
            value = None
            values_list.append(value)
            entry.configure(background="pink")
        elif is_valid(value):
            value = float(value)
            values_list.append(value)
            entry.configure(state=tk.DISABLED, disabledbackground='light green')
        else:
            blink_warning()
    # print(values_list)  # check that validation was successful
    try:
        comp.given(velocity=values_list[0], change_velocity=values_list[1], initial_velocity=values_list[2],
                   final_velocity=values_list[3],
                   acceleration=values_list[4], change_acceleration=values_list[5], time=values_list[6],
                   change_time=values_list[7],
                   distance=values_list[8], change_distance=values_list[9], momentum=values_list[10],
                   change_momentum=values_list[11], mass=values_list[12],
                   potential_energy=values_list[13], kinetic_energy=values_list[14], height=values_list[15],
                   net_force=values_list[16],
                   impulse=values_list[17], force=values_list[18])
    except:
        blink_warning()
    else:
        fetch_results()


def fetch_results():
    available_list = comp.available()
    for available in available_list:  # peak performance
        for entry in entry_list:
            if available == entry.winfo_name():
                entry.configure(background='light blue')


reset_image = tk.PhotoImage(file='assets/AdobeStock_374462435.png')
reset_image = reset_image.subsample(50)

search_image = tk.PhotoImage(file='assets/AdobeStock_227446387.png')
search_image = search_image.subsample(50)

go_button = tk.Button(button_frame, image=search_image, command=submit_variables, font=stat_font, borderwidth=0)
no_button = tk.Button(button_frame, image=reset_image, command=reset_entrys, font=stat_font, borderwidth=0)
no_button.pack(side=tk.LEFT, anchor='center', fill=tk.NONE, expand=tk.NO, padx=20, pady=3)
go_button.pack(side=tk.LEFT, anchor='center', fill=tk.NONE, expand=tk.NO, padx=20, pady=3)

button_frame.pack(side=tk.BOTTOM, fill=tk.NONE, expand=tk.NO)
label_column_one.pack(side=tk.LEFT)
entry_column_one.pack(side=tk.LEFT)
label_column_two.pack(side=tk.LEFT)
entry_column_two.pack(side=tk.LEFT)

master.bind('<Return>', lambda event: submit_variables())
master.bind('<F5>', lambda event: reset_entrys())

master.update()

button_frame_width = button_frame.winfo_width()
reset_button_width = no_button.winfo_width()
search_button_width = go_button.winfo_width()

master.mainloop()
