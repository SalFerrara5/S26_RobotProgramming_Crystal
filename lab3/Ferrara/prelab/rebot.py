class Robot:
    """
    Robot class containing ID number, status (online/offline),
    and location (cell position such as A3).
    """

    def __init__(self, id_number, status, location):
        self.id_number = id_number
        self.status = status
        self.location = location

    def __str__(self):
        state = "Online" if self.status else "Offline"
        return f"Robot {self.id_number} is {state} at location {self.location}"

    def moveBot(self, new_location):
        self.location = new_location

    def changeStatus(self):
        self.status = not self.status

