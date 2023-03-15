import tkinter as tk
from time import sleep
from tkinter import messagebox
from PIL import Image, ImageTk
from physics import Physics

master = tk.Tk()
comp = Physics()

# master.resizable("false", "false")
master.resizable(False, False)

stat_font = ("Arial", 20)

label_column = tk.Frame(master)
entry_column = tk.Frame(master)
button_frame = tk.Frame(master)

velocity_label = tk.Label(label_column, text="Velocity:", font=stat_font)
mass_label = tk.Label(label_column, text="Mass:", font=stat_font)
acceleration_label = tk.Label(label_column, text="Acceleration:", font=stat_font)
distance_label = tk.Label(label_column, text="Distance:", font=stat_font)
time_label = tk.Label(label_column, text="Time:", font=stat_font)
momentum_label = tk.Label(label_column, text="Momentum:", font=stat_font)
initial_velocity = tk.Label(label_column, text="Init. Velocity:", font=stat_font)

velocity_label.pack(side=tk.TOP, anchor='e')  # , anchor=tk.NW
mass_label.pack(side=tk.TOP, anchor='e')
acceleration_label.pack(side=tk.TOP, anchor='e', pady=2)
distance_label.pack(side=tk.TOP, anchor='e')
time_label.pack(side=tk.TOP, anchor='e')
momentum_label.pack(side=tk.TOP, anchor='e', pady=2)
initial_velocity.pack(side=tk.TOP, anchor='e')

velocity_entry = tk.Entry(entry_column, width=8, name='velocity', font=stat_font)
mass_entry = tk.Entry(entry_column, width=8, name='mass', font=stat_font)
acceleration_entry = tk.Entry(entry_column, width=8, name='acceleration', font=stat_font)
distance_entry = tk.Entry(entry_column, width=8, name='distance', font=stat_font)
time_entry = tk.Entry(entry_column, width=8, name='time', font=stat_font)
momentum_entry = tk.Entry(entry_column, width=8, name='momentum', font=stat_font)
initial_velocity_entry = tk.Entry(entry_column, width=8, name='initial_velocity', font=stat_font)

velocity_entry.pack(side=tk.TOP, anchor=tk.NW, pady=2)
mass_entry.pack(side=tk.TOP, anchor=tk.NW, pady=2)
acceleration_entry.pack(side=tk.TOP, anchor=tk.NW, pady=2)
distance_entry.pack(side=tk.TOP, anchor=tk.NW, pady=2)
time_entry.pack(side=tk.TOP, anchor=tk.NW, pady=2)
momentum_entry.pack(side=tk.TOP, anchor=tk.NW, pady=2)
initial_velocity_entry.pack(side=tk.TOP, anchor=tk.NW, pady=2)

entry_list = [velocity_entry, mass_entry, acceleration_entry, distance_entry, time_entry, momentum_entry,
              initial_velocity_entry]

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
    print(values_list)  # check that validation was successful
    try:
        comp.given(velocity=values_list[0], mass=values_list[1], acceleration=values_list[2], distance=values_list[3],
                   time=values_list[4], momentum=values_list[5], initial_velocity=entry_list[6])
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
        elif available == 'initial_velocity':
            entry_list[6].configure(background='light blue')


reset_img4 = tk.PhotoImage(file='reset_.png')


go_button = tk.Button(button_frame, text="->", command=submit_variables, font=stat_font)
no_button = tk.Button(button_frame, image=reset_img4, command=reset_entrys, font=stat_font, borderwidth=0)
go_button.pack(side=tk.RIGHT, anchor='center', fill=tk.NONE, expand=tk.NO, padx=50, pady=3)
no_button.pack(side=tk.LEFT, anchor='center', fill=tk.NONE, expand=tk.NO, padx=50, pady=3)

button_frame.pack(side=tk.BOTTOM, fill=tk.NONE, expand=tk.NO)
label_column.pack(side=tk.LEFT)
entry_column.pack(side=tk.RIGHT)

master.bind('<Return>', lambda event: submit_variables())
master.bind('<F5>', lambda event: reset_entrys())
# master.bind('<BackSpace>', lambda event: fetch_results())  # testing/debugging
master.update()
my_width = acceleration_label.winfo_width()
print(my_width)

master.mainloop()
