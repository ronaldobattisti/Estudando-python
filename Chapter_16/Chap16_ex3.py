class Elevator:

    def __init__(self, maxfloor, qperson, actualperson):
        self._actualfloor = 0
        self._maxfloor = maxfloor
        self._qperson = qperson
        self._actualperson = actualperson

    def get_floor(self):
        return self._actualfloor

    def set_floor(self, floor):
        self._actualfloor = floor

    def get_maxfloor(self):
        return self._maxfloor

    def set_maxfloor(self, maxfloor):
        self._maxfloor = maxfloor

    def get_qperson(self):
        return self._qperson

    def set_qperson(self, qperson):
        self._qperson = qperson

    def get_actualperson(self):
        return self._actualperson

    def set_actualperson(self, actualperson):
        self._actualperson = actualperson

    def enter(self, quant):
        if quant + self.get_actualperson() <= self.get_qperson():
            self.set_actualperson(quant + self.get_actualperson())
            print(
                f"You entered, now that's {self.get_actualperson()} person in the elevator, the limit is {self.get_qperson()}")
        else:
            print(
                f"You can't enter, the limit is {self.get_qperson()} and would have {quant + self.get_actualperson()} person")

    def get_out(self, quant):
        if quant <= self.get_actualperson():
            self.set_actualperson(self.get_actualperson() - quant)
            print(
                f"{quant} person left, now that's {self.get_actualperson()} person in the ellevator")
        else:
            print(
                f"Incorrect input {quant} person are lefting but that's only {self.get_actualperson()}")

    def up(self, quant):
        if self.get_maxfloor() >= (quant + self.get_floor()):
            self.set_floor(quant + self.get_floor())
            print(f"Now we are at {self.get_floor()}º floor")
        else:
            print(
                f"Incorrect input, we are at {self.get_floor()}º floor and that's only {self.get_maxfloor()}º floor, you're trying to go to the {quant + self.get_floor()}º floor")

    def down(self, quant):
        if self.get_floor() - quant >= 0:
            self.set_floor(self.get_floor() - quant)
            print(f"Now we are at {self.get_floor()}º floor")
        else:
            print(
                f"Incorrect input, we are at {self.get_floor()}º floor and you're trying to go down {quant} floors, so you will be at {self.get_floor() - quant}º floor")


el = Elevator(10, 10, 0)

while True:
    print("Select a opption: ")
    try:
        ind = int(input("1 - Enter\n2 - Exit\n3 - Up\n4 - Down\n"))
        if ind == 1:
            quant = int(
                input("Input the number of person thar are entering: "))
            el.enter(quant)
        elif ind == 2:
            quant = int(
                input("Input the number of person thar are getting out: "))
            el.get_out(quant)
        elif ind == 3:
            quant = int(input("How much floors you want to climb: "))
            el.up(quant)
        elif ind == 4:
            quant = int(input("How much floors you want to go down: "))
            el.down(quant)
    except ValueError as e:
        print(f"The input should be a integer: {e}")
