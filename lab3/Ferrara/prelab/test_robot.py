from robot import Robot

robot1 = Robot(101, True, "A3")
robot2 = Robot(102, False, "B7")

print(robot1)
print(robot2)

robot1.moveBot("C5")
print("\nAfter moving robot1:")
print(robot1)

robot2.changeStatus()
print("\nAfter changing robot2 status:")
print(robot2)

