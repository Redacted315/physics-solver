import tkinter as tk
from physics import Physics
from tooltip import *
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
button_frame = tk.Frame(master)

velo_image = tk.PhotoImage(file='assets/velocity.png')
acc_image = tk.PhotoImage(file='assets/acceleration.png')
time_image = tk.PhotoImage(file='assets/time.png')
dist_image = tk.PhotoImage(file='assets/distance.png')
disp_image = tk.PhotoImage(file='assets/displacement.png')
mom_image = tk.PhotoImage(file='assets/momentum.png')
mass_image = tk.PhotoImage(file='assets/mass.png')
pot_image = tk.PhotoImage(file='assets/potential.png')
kin_image = tk.PhotoImage(file='assets/kinetic.png')
impulse_image = tk.PhotoImage(file='assets/impulse.png')
force_image = tk.PhotoImage(file='assets/force.png')

velocity_label = tk.Label(label_column_one, image=velo_image, font=stat_font)
velocity_label.grid(row=0, column=0)
acceleration_label = tk.Label(label_column_one, image=acc_image, font=stat_font)
acceleration_label.grid(row=1, column=0)
time_label = tk.Label(label_column_one, image=time_image, font=stat_font)
time_label.grid(row=2, column=0)
distance_label = tk.Label(label_column_one, image=dist_image, font=stat_font)
distance_label.grid(row=3, column=0)
displacement_label = tk.Label(label_column_one, image=disp_image, font=stat_font)
displacement_label.grid(row=4, column=0)
momentum_label = tk.Label(label_column_one, image=mom_image, font=stat_font)
momentum_label.grid(row=5, column=0)
mass_label = tk.Label(label_column_two, image=mass_image, font=stat_font)
mass_label.grid(row=0, column=0)
potential_energy_label = tk.Label(label_column_two, image=pot_image, font=stat_font)
potential_energy_label.grid(row=1, column=0)
kinetic_energy_label = tk.Label(label_column_two, image=kin_image, font=stat_font)
kinetic_energy_label.grid(row=2, column=0)
impulse_label = tk.Label(label_column_two, image=impulse_image, font=stat_font)
impulse_label.grid(row=3, column=0)
force_label = tk.Label(label_column_two, image=force_image, font=stat_font)
force_label.grid(row=4, column=0)
# <labels entrys>
velocity_entry = tk.Entry(entry_column_one, font=stat_font, width=8, name='velocity')
velocity_entry.grid(row=0, column=0, padx=2, pady=4)
acceleration_entry = tk.Entry(entry_column_one, font=stat_font, width=8, name='acceleration')
acceleration_entry.grid(row=1, column=0, padx=2, pady=4)
time_entry = tk.Entry(entry_column_one, font=stat_font, width=8, name='time')
time_entry.grid(row=2, column=0, padx=2, pady=4)
distance_entry = tk.Entry(entry_column_one, font=stat_font, width=8, name='distance')
distance_entry.grid(row=3, column=0, padx=2, pady=4)
displacement_entry = tk.Entry(entry_column_one, font=stat_font, width=8, name='displacement')
displacement_entry.grid(row=4, column=0, padx=2, pady=4)
momentum_entry = tk.Entry(entry_column_one, font=stat_font, width=8, name='momentum')
momentum_entry.grid(row=5, column=0, padx=2, pady=4)
mass_entry = tk.Entry(entry_column_two, font=stat_font, width=8, name='mass')
mass_entry.grid(row=0, column=0, padx=2, pady=4)
potential_energy_entry = tk.Entry(entry_column_two, font=stat_font, width=8, name='energy_potential')
potential_energy_entry.grid(row=1, column=0, padx=2, pady=4)
kinetic_energy_entry = tk.Entry(entry_column_two, font=stat_font, width=8, name='energy_kinetic')
kinetic_energy_entry.grid(row=2, column=0, padx=2, pady=4)
impulse_entry = tk.Entry(entry_column_two, font=stat_font, width=8, name='impulse')
impulse_entry.grid(row=3, column=0, padx=2, pady=4)
force_entry = tk.Entry(entry_column_two, font=stat_font, width=8, name='force')
force_entry.grid(row=4, column=0, padx=2, pady=4)
entry_list = [velocity_entry, acceleration_entry, time_entry, distance_entry, displacement_entry, momentum_entry,
              mass_entry, potential_energy_entry, kinetic_energy_entry, impulse_entry, force_entry]


def reset_entrys():
    for entry in entry_list:
        entry.configure(background='SystemWindow', state='normal')
        entry.delete(0, tk.END)
        master.focus()  # remove cursor focus from entry's


def submit_variables():
    comp.given(velocity=velocity_entry.get(), acceleration=acceleration_entry.get(), time=time_entry.get(),
               distance=distance_entry.get(), displacement=displacement_entry.get(), momentum=momentum_entry.get(),
               mass=mass_entry.get(), potential_energy=potential_energy_entry.get(),
               kinetic_energy=kinetic_energy_entry.get(), impulse=impulse_entry.get(), force=force_entry.get())
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
reset_button = tk.Button(button_frame, image=reset_image, command=reset_entrys, font=stat_font, borderwidth=0)
reset_button.pack(side=tk.LEFT, anchor='center', fill=tk.NONE, expand=tk.NO, padx=20, pady=3)
go_button.pack(side=tk.LEFT, anchor='center', fill=tk.NONE, expand=tk.NO, padx=20, pady=3)

CreateToolTip(reset_button, text='Reset')
CreateToolTip(go_button, text='Go')
CreateToolTip(velocity_label, text='Velocity (m/s)')
CreateToolTip(acceleration_label, text='Acceleration (m/s^2)')
CreateToolTip(time_label, text='Time (s)')
CreateToolTip(distance_label, text='Distance (m)')
CreateToolTip(displacement_label, text='Displacement (m)')
CreateToolTip(momentum_label, text='Momentum (kg*m/s)')
CreateToolTip(mass_label, text='Mass (kg)')
CreateToolTip(potential_energy_label, text='Potential Energy (J)')
CreateToolTip(kinetic_energy_label, text='Kinetic Energy (J)')
CreateToolTip(impulse_label, text='Impulse (N*s)')
CreateToolTip(force_label, text='Force (N)')

button_frame.pack(side=tk.BOTTOM, fill=tk.NONE, expand=tk.NO)
label_column_one.pack(side=tk.LEFT)
entry_column_one.pack(side=tk.LEFT)
label_column_two.pack(side=tk.LEFT)
entry_column_two.pack(side=tk.LEFT)

master.bind('<Return>', lambda event: submit_variables())
master.bind('<F5>', lambda event: reset_entrys())

master.update()

master.mainloop()
