import tkinter as tk
from physics import Physics
from tooltip import *
import webbrowser
import sys


class App():
    
    def __init__(self, root):
        self.root = root
        self.comp = Physics()
        self.root.title("App")
        self.root.geometry("190x380")
        self.root.resizable(False, False)
        self.root.iconbitmap("assets/icon.ico")
        self.root.option_add('*tearOff', False)
        self.stat_font = ("Arial", 20)

        self.menu_bar = tk.Menu(self.root)
        self.root['menu'] = self.menu_bar
        self.menu_options = tk.Menu(self.menu_bar)
        self.menu_edit = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(menu=self.menu_options, label='Options')
        self.menu_bar.add_cascade(menu=self.menu_edit, label='Help')
        self.menu_options.add_command(label='Coming soon...', state='disabled', activebackground='SystemMenu')
        self.menu_options.add_command(label='Close', command=self.kill_self)
        self.menu_edit.add_command(label='Shortcuts', command=self.open_shortcut)
        self.menu_edit.add_command(label='Help', command=self.link_github)

        self.velo_image = tk.PhotoImage(file='assets/velocity.png');self.acc_image = tk.PhotoImage(file='assets/acceleration.png');self.time_image = tk.PhotoImage(file='assets/time.png');self.dist_image = tk.PhotoImage(file='assets/distance.png');self.disp_image = tk.PhotoImage(file='assets/displacement.png');self.mom_image = tk.PhotoImage(file='assets/momentum.png');self.mass_image = tk.PhotoImage(file='assets/mass.png');self.pot_image = tk.PhotoImage(file='assets/potential.png');self.kin_image = tk.PhotoImage(file='assets/kinetic.png');self.impulse_image = tk.PhotoImage(file='assets/impulse.png');self.force_image = tk.PhotoImage(file='assets/force.png')
        self.velo_var = tk.IntVar();self.acceleration_var = tk.IntVar();self.time_var = tk.IntVar();self.distance_var = tk.IntVar();self.displacement_var = tk.IntVar();self.momentum_var = tk.IntVar();self.mass_var = tk.IntVar();self.potential_energy_var = tk.IntVar();self.kinetic_energy_var = tk.IntVar();self.impulse_var = tk.IntVar();self.force_var = tk.IntVar()
        self.intvarlist = [self.velo_var, self.acceleration_var, self.time_var, self.distance_var, self.displacement_var, self.momentum_var, self.mass_var, self.potential_energy_var, self.kinetic_energy_var, self.impulse_var, self.force_var]
        self.placelist = [ [45, 15], [45, 65], [45, 115], [45, 165], [45, 215], [45, 265], [150, 25], [150, 80], [150, 130], [150, 180], [150, 230] ]
        self.labelcoords = [ [1, 20], [1, 70], [1, 120], [1, 170], [1, 220], [1, 270], [100, 30], [100, 80], [100, 130], [85, 180], [100, 230] ]
        self.variable_list = [
            "velocity",
            "acceleration",
            "time",
            "distance",
            "displacement",
            "momentum",
            "mass",
            "potential_energy",
            "kinetic_energy",
            "impulse",
            "force"
            ]
        self.description = ['Velocity (m/s)', 'Acceleration (m/s^2)', 'Time (s)', 'Distance (m)', 'Displacement (m)', 'Momentum (kg*m/s)', 'Mass (kg)', 'Potential Energy (J)', 'Kinetic Energy (J)', 'Impulse (N*s)', 'Force (N)']
        self.image_list = [self.velo_image, self.acc_image, self.time_image, self.dist_image, self.disp_image, self.mom_image, self.mass_image, self.pot_image, self.kin_image, self.impulse_image, self.force_image]
        self.buttonlist = []

        #  Loop to create checkboxes
        for a, b in enumerate(self.variable_list): #  a in index, b is item
            self.checkbutton = tk.Checkbutton(self.root, name=b, variable=self.intvarlist[a])
            x_coord = None
            y_coord = None
            for i in self.placelist[a]:
                if not x_coord:
                    x_coord = i
                    continue
                y_coord = i
            self.checkbutton.place(x=x_coord, y=y_coord)
            self.buttonlist.append(self.checkbutton)
        
        #  Loop to create labels
        for c, d in enumerate(self.variable_list): #  a in index, b is item
            self.variable_label = tk.Label(self.root, image=self.image_list[c])
            CreateToolTip(self.variable_label, text=self.description[c])
            x_coord_label = None
            y_coord_label = None
            for f in self.labelcoords[c]:
                if not x_coord_label:
                    x_coord_label = f
                    continue
                y_coord_label = (f - 15)
            self.variable_label.place(x=x_coord_label, y=y_coord_label)
        self.submit_button = tk.Button(self.root, text="Sumbit", command=self.submit_variables, width=10, height=2)
        self.submit_button.place(x=55, y=305)
        CreateToolTip(self.submit_button, text="Or Press The Enter Key!")

        self.root.bind('<Return>', lambda event: self.submit_variables())  
        self.root.bind('<F5>', lambda event: self.reset())

        self.root.update()
        self.root.mainloop()

    def reset(self):
            for checkbutton in self.buttonlist:
                checkbutton.deselect()
            self.root.focus()
            self.comp.clear()

    def submit_variables(self):
        # self.comp.given(velocity=self.velo_var.get(), acceleration=self.acceleration_var.get(), time=self.time_var.get(),
        #            distance=self.distance_var.get(), displacement=self.displacement_var.get(), momentum=self.momentum_var.get(),
        #            mass=self.mass_var.get(), potential_energy=self.potential_energy_var.get(),
        #            kinetic_energy=self.kinetic_energy_var.get(), impulse=self.impulse_var.get(), force=self.force_var.get())
        # self.fetch_results()
        if self.velo_var.get():
            print("velocity is checked")
        elif not self.velo_var.get():
            print("velocity is not checked")

    def fetch_results(self):
        available_list = self.comp.available()
        for available in available_list:  # peak performance
            for button in self.checkbutton_list:
                if available == button.winfo_name():
                    print(available)

    def callback(self, url):
        webbrowser.open_new_tab(url)

    def link_github(self):
        github = tk.Toplevel(self.root)
        github.geometry("300x70")
        link = tk.Label(github, text='Contribute on GitHub!', font='Arial 12 underline', fg='blue')
        link.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        link.bind("<Button-1>", lambda e: self.callback("https://github.com/Redacted315/physics-solver"))

    def kill_self(self):
        sys.exit(727)
    
    def open_shortcut(self):
        self.callback("shortcuts.html")


def main():
    master = tk.Tk()
    my_app = App(master)
    master.mainloop()


if __name__ == "__main__":
    main()
