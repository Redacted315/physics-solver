"""
To Do:
    create another requirement dict for variables with multiple 'recipes'
    ex.
        [in class Physics: __init__]
        self.alternativeRequirementDict = {...}
"""


class Physics:
    def __init__(self):
        self.known = None
        self.variableDict = dict(velocity=None, change_velocity=None, initial_velocity=None, final_velocity=None,
                                 acceleration=None, change_acceleration=None, time=None, change_time=None,
                                 distance=None, change_distance=None, momentum=None, change_momentum=None, mass=None,
                                 potential_energy=None, kinetic_energy=None, height=None, net_force=None,
                                 impulse=None, force=None)

        self.requirementDict = dict(mass=['momentum', 'velocity'], momentum=['mass', 'velocity'],
                                    velocity=['change_distance', 'change_time'],
                                    acceleration=['change_velocity', 'change_time'],
                                    distance=['initial_velocity', 'time', 'acceleration'],
                                    time=['change_distance', 'velocity'],
                                    potential_energy=['mass', 'height'], force=['mass', 'acceleration'],
                                    impulse=['mass', 'change_velocity'], kinetic_energy=['mass', 'velocity'])
        self.possible = []

    def given(self, **known):
        self.known = known
        for variable in self.variableDict:
            if variable in list(known.keys()):
                self.variableDict[variable] = known[variable]
        self.variableDict = self.variableDict

    def available(self):
        for key in self.requirementDict:
            if self.variableDict[key] is None:
                reqs = len(self.requirementDict[key])
                reqs_met = 0
                for i in self.requirementDict[key]:
                    if self.variableDict[i] is None:
                        pass
                    else:
                        reqs_met += 1
                        if reqs_met == reqs:
                            self.possible.append(key)
        return self.possible


"""
requirements:

m(Ep,h)#equations line 25
m(F,∆t,∆v)#equations line 21
impulse(m,∆v)
impulse(F,∆t)
d(vf,t,a)#equations line 9
d(vi,vf,t)
t(∆v,a)
Ek(m,v)Ek = 0.5 * m * v^2
F(∆t,∆v,m)#equations line 21
∆v(F,∆t,m)#equations line 21
∆t(m,∆v,F)#equations line 21
-m(p,v)
-p(m,v)
-v(∆d,∆t)
-F(m,a)
-a(∆v,∆t)
-t(∆d,v)
-Ep(m,h)
-d(vi,t,a)#equations line 7

"""
