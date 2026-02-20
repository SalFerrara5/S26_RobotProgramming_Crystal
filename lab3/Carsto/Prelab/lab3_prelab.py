class Robot:
    """
    A class to represent a robot with ID, status, and location tracking.
    """
    
    def __init__(self, robot_id, location="A1", online=True):
        """
        Initialize a Robot instance.
        
        Args:
            robot_id: Unique identifier for the robot
            location: Cell location (e.g., 'A3')
            online: Boolean flag for online/offline status (default: True)
        """
        self.id = robot_id
        self.online = online
        self.location = location
    
    def moveBot(self, new_location):
        """
        Move the robot to a new location.
        
        Args:
            new_location: The new cell location (e.g., 'B5')
        """
        old_location = self.location
        self.location = new_location
        print(f"Robot {self.id} moved from {old_location} to {new_location}")
    
    def changeStatus(self):
        """
        Toggle the robot's online/offline status.
        """
        self.online = not self.online
        status_str = "online" if self.online else "offline"
        print(f"Robot {self.id} is now {status_str}")
    
    def __str__(self):
        """
        String representation of the Robot.
        """
        status_str = "online" if self.online else "offline"
        return f"Robot {self.id}: {status_str} at {self.location}"


# Verification script
if __name__ == "__main__":
    print("=== Robot Class Verification ===\n")
    
    # Create a robot instance
    robot1 = Robot(robot_id=101, location="A3", online=True)
    print(f"Created: {robot1}\n")
    
    # Test moveBot method
    print("Testing moveBot:")
    robot1.moveBot("B5")
    robot1.moveBot("C2")
    print(f"Current state: {robot1}\n")
    
    # Test changeStatus method
    print("Testing changeStatus:")
    robot1.changeStatus()  # Should go offline
    print(f"Current state: {robot1}\n")
    
    robot1.changeStatus()  # Should go back online
    print(f"Current state: {robot1}\n")
    
    # Create another robot to verify independence
    print("Creating second robot:")
    robot2 = Robot(robot_id=202, location="D1", online=False)
    print(f"Created: {robot2}\n")
    
    print("Final status of both robots:")
    print(robot1)
    print(robot2)
