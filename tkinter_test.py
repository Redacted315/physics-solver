import tkinter as tk
from time import sleep
from tkinter import messagebox

from main import Physics

master = tk.Tk()
comp = Physics()

# master.resizable("false", "false")
master.resizable(False, False)

label_column = tk.Frame(master)
entry_column = tk.Frame(master)
button_frame = tk.Frame(master)

velocity_label = tk.Label(label_column, text="Velocity:")
mass_label = tk.Label(label_column, text="Mass:")
acceleration_label = tk.Label(label_column, text="Acceleration:")
distance_label = tk.Label(label_column, text="Distance:")
time_label = tk.Label(label_column, text="Time:")
momentum_label = tk.Label(label_column, text="Momentum:")

velocity_label.pack(side=tk.TOP, anchor=tk.NW)
mass_label.pack(side=tk.TOP, anchor=tk.NW)
acceleration_label.pack(side=tk.TOP, anchor=tk.NW, pady=2)
distance_label.pack(side=tk.TOP, anchor=tk.NW)
time_label.pack(side=tk.TOP, anchor=tk.NW)
momentum_label.pack(side=tk.TOP, anchor=tk.NW, pady=2)

velocity_entry = tk.Entry(entry_column, width=8, name='velocity')
mass_entry = tk.Entry(entry_column, width=8, name='mass')
acceleration_entry = tk.Entry(entry_column, width=8, name='acceleration')
distance_entry = tk.Entry(entry_column, width=8, name='distance')
time_entry = tk.Entry(entry_column, width=8, name='time')
momentum_entry = tk.Entry(entry_column, width=8, name='momentum')

velocity_entry.pack(side=tk.TOP, anchor=tk.NW, pady=2)
mass_entry.pack(side=tk.TOP, anchor=tk.NW, pady=2)
acceleration_entry.pack(side=tk.TOP, anchor=tk.NW, pady=2)
distance_entry.pack(side=tk.TOP, anchor=tk.NW, pady=2)
time_entry.pack(side=tk.TOP, anchor=tk.NW, pady=2)
momentum_entry.pack(side=tk.TOP, anchor=tk.NW, pady=2)

entry_list = [velocity_entry, mass_entry, acceleration_entry, distance_entry, time_entry, momentum_entry]

original_background_colour = velocity_entry.cget("background")


def warning_background():  # flashes entry background colour
    for i in entry_list:
        i.configure(state='disabled', disabledbackground='#ebd36c')  # yellow
    master.update_idletasks()
    sleep(0.2)
    for i in entry_list:
        i.configure(state='disabled', disabledbackground='#bf6e60')  # red
    master.update_idletasks()
    sleep(0.2)


def blink_warning():
    import winsound
    # Play Windows exit sound.
    winsound.PlaySound('SystemHand', winsound.SND_ASYNC)
    # .SND_ASYNC returns immediately, without this none of the following code will execute until
    # the sound has finished playing in its entirety
    for i in range(3):
        warning_background()


def reset_entrys():
    for i in entry_list:
        i.configure(background=original_background_colour, state='normal')
        i.delete(0, tk.END)
        master.focus()  # remove cursor focus from entry's


class UnacceptableInputType(Exception):
    """Raised when the input value is not a float"""
    pass


def is_valid(value):
    try:
        float(value)
        return True
    except TypeError:
        return False


# noinspection PyBroadException
def submit_variables():
    values_list = []
    for i in entry_list:
        value = i.get()
        if value == '':
            value = None
            values_list.append(value)
            i.configure(background="pink")
        elif is_valid(value):
            value = float(value)
            values_list.append(value)
            i.configure(state=tk.DISABLED, disabledbackground='light green')
        else:
            messagebox.showerror(title='oopsie!', message=value)
    # print(values_list) # check that validation was successful
    try:
        comp.given(velocity=values_list[0], mass=values_list[1], acceleration=values_list[2], distance=values_list[3],
                   time=values_list[4], momentum=values_list[5])
    except:
        blink_warning()
    else:
        fetch_results()


def fetch_results():
    available_list = comp.available()
    for available in available_list:  # peak performance
        if available == 'mass':
            entry_list[1].configure(background='light blue')
        elif available == 'velocity':
            entry_list[0].configure(background='light blue')
        elif available == 'acceleration':
            entry_list[2].configure(background='light blue')
        elif available == 'distance':
            entry_list[3].configure(background='light blue')
        elif available == 'time':
            entry_list[4].configure(background='light blue')
        elif available == 'momentum':
            entry_list[5].configure(background='light blue')


go_button = tk.Button(button_frame, text="GO", command=submit_variables)
no_button = tk.Button(button_frame, text="NO", command=reset_entrys)
go_button.pack(side=tk.RIGHT, anchor='ne', fill=tk.X, expand=tk.YES)
no_button.pack(side=tk.LEFT, anchor='nw', fill=tk.X, expand=tk.YES)

button_frame.pack(side=tk.BOTTOM, fill=tk.X, expand=tk.YES)
label_column.pack(side=tk.LEFT)
entry_column.pack(side=tk.RIGHT)

master.bind('<Return>', lambda event: submit_variables())
master.bind('<F5>', lambda event: reset_entrys())
master.bind('<BackSpace>', lambda event: fetch_results())  # testing/debugging

master.mainloop()
