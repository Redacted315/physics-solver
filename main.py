import math

class physics:
    def __init__(self):
        self.variableDict = {"velocity":None ,"change_velocity":None,"initial_velocity":None,"final_velocity":None,"acceleration":None,"change_acceleration":None,
                             "time":None,"change_time":None,"distance":None,"change_distance":None,"momentum":None,"change_momentum":None,
                             "mass":None,"potential_energy":None,"kinetic_energy":None,"height":None,"net_force":None}
    def given(self, **known):
        self.known = known
        # known is dict
        # if arguments passsed to func given 'v=14, d=37.9'
        # known.keys() > ['v', 'd']
        # known.values() > [14, 37.9]
        for variable in self.variableDict:
            if variable in list(known.keys()):
                self.variableDict[variable] = known[variable]
        print(self.variableDict)
        self.variableDict = self.variableDict
        for variable in self.variableDict:
            if self.variableDict[variable] is not None:
                print(variable + " is known")
    def available(self):
        if self.variableDict["velo"] is not None and self.variableDict["mass"] is not None:
            return "you can calculate momentum > m * v = p"
lightningMcqueen = physics()
lightningMcqueen.given(velo=1.2, mass=0.5, dist=134)
print(lightningMcqueen.available())


"""
requirements:

m(p,v)
m(Ep,h)#equations line 25
p(m,v)
v(∆d,∆t)
a(∆v,∆t)
t(∆d,v)
t(∆v,a)
Ek(m,v)
Ep(m,h)
impulse(m,∆v)
impulse(F,∆t)
d(vi,t,a)
d(vf,t,a)
d(vi,vf,t)

"""