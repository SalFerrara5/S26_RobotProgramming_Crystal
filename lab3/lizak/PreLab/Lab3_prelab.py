class Robot:
    """
    Represents a robot with an ID, online/offline status, and a location.
    """

    def __init__(self, robot_id, status=False, location="A1"):
        """
        Parameters:
        robot_id : int
            Unique robot identification number
        status : bool
            True = online, False = offline
        location : str
            Grid cell location (e.g., 'A3')
        """
        self.robot_id = robot_id
        self.status = status
        self.location = location

    def __str__(self):
        state = "Online" if self.status else "Offline"
        return f"Robot {self.robot_id} | Status: {state} | Location: {self.location}"

    def moveBot(self, new_location):
        """
        Move the robot to a new location.
        """
        self.location = new_location

    def changeStatus(self):
        """
        Toggle the robot's online/offline status.
        """
        self.status = not self.status

