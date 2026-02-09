class Robot:
    def __init__(self, robot_id, status=False, location="A1"):
        self.robot_id = robot_id
        self.status = status
        self.location = location

    def __str__(self):
        state = "Online" if self.status else "Offline"
        return f"Robot {self.robot_id} | Status: {state} | Location: {self.location}"

    def moveBot(self, new_location):
        if not self.status:
            print("Cannot move robot: Robot is currently offline.")
            return
        self.location = new_location
        print(f"Robot moved to {new_location}")

    def changeStatus(self):
        self.status = not self.status
        state = "Online" if self.status else "Offline"
        print(f"Robot is now {state}")

