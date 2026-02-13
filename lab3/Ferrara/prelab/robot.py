class Robot:
    def __init__(self, id_number, status=False, location="A1"):
        self.id_number = id_number
        self._status = status
        self.location = location

    def __str__(self):
        state = "Online" if self._status else "Offline"
        return f"Robot {self.id_number} is {state} at location {self.location}"

    def turnOn(self):
        self._status = True

    def turnOff(self):
        self._status = False

    def toggleStatus(self):
        self._status = not self._status

    def moveBot(self, new_location):
        if not self._status:
            print("Robot is OFF. Cannot move.")
            return
        self.location = new_location

