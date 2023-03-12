import math

"""
To Do:
    - expand self.requirementsDict with info from docstring at end of file
    - start developing gui, maybe with pysimplegui so its not as yucky lookin'
"""


class physics:
    def __init__(self):
        self.variableDict = {"velocity":None ,"change_velocity":None,"initial_velocity":None,"final_velocity":None,"acceleration":None,"change_acceleration":None,
                             "time":None,"change_time":None,"distance":None,"change_distance":None,"momentum":None,"change_momentum":None,
                             "mass":None,"potential_energy":None,"kinetic_energy":None,"height":None,"net_force":None,"applied_force":None,"impulse":None}
        self.requirementDict = {"mass":['momentum','velocity'],"momentum":['mass','velocity'],"velocity":['change_distance','change_time'],"acceleration":['change_velocity','change_time']}
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
-m(p,v)
m(Ep,h)#equations line 25
-p(m,v)
-v(∆d,∆t)
a(∆v,∆t)
t(∆d,v)
t(∆v,a)
Ek(m,v)Ek = 0.5 * m * v^2
Ep(m,h)
impulse(m,∆v)
impulse(F,∆t)
d(vi,t,a)
d(vf,t,a)
d(vi,vf,t)
F(m,a)
F(∆t,∆v,m)#equations line 21
m(F,∆t,∆v)#equations line 21
∆v(F,∆t,m)#equations line 21
∆t(m,∆v,F)#equations line 21
"""
