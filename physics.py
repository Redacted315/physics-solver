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
        self.variableDict = dict(velocity=None, acceleration=None, time=None, distance=None, displacement=None,
                                 momentum=None, mass=None, potential_energy=None, kinetic_energy=None,
                                 impulse=None, force=None)

        self.requirementDict = dict(velocity=[['distance', 'time'], ['displacement', 'time']],
                                    distance=[['velocity', 'time']],
                                    displacement=[['velocity', 'time']],
                                    time=[['distance', 'velocity'], ['displacement', 'velocity']],
                                    acceleration=[['velocity', 'time']],
                                    momentum=[['mass', 'velocity']],
                                    impulse=[['mass', 'velocity'], ['force', 'time']])
        self.possible = []

    def given(self, **known):
        self.known = known
        for i in self.known:
            if self.known[i] == '':
                self.known[i] = None
        for variable in self.variableDict:
            if variable in list(known.keys()):
                self.variableDict[variable] = known[variable]
        self.variableDict = self.variableDict

    def available(self):
        for key in self.requirementDict:
            for required_list in self.requirementDict[key]:
                reqs = len(required_list)
                reqs_met = 0
                if self.variableDict[key] is None or self.variableDict[key] is False:
                    for variable in required_list:
                        if self.variableDict[variable] is None:
                            pass
                        else:
                            reqs_met += 1
                            if reqs_met == reqs:
                                self.possible.append(key)
        return self.possible

    def clear(self):
        self.__init__()


"""
requirements:

v = ∆d / ∆t

a = ∆v / ∆t

p = m * v

F * ∆t = m * ∆v

Ek = 0.5 * m * v^2

Ep = m * g * h

"""
