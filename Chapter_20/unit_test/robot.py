class Robot:

    def __init__(self, name, battery=100, skills=[]):
        self._name = name
        self._battery = battery
        self._skills = skills

    @property
    def name(self):
        return self._name

    @property
    def battery(self):
        return self._battery

    @property
    def skills(self):
        return self._skills

    def charge(self):
        self._battery = 100

    def say_name(self):
        if self._battery > 0:
            self._battery -= 1
            return f"Beep Boop I'm {self._name}"
        return "Low battery"

    def new_skill(self, new_skill, charge):
        if self._battery >= charge:
            self._battery -= charge
            self._skills.append(new_skill)
            return f"I've learned {new_skill}"
        return "low battery"
