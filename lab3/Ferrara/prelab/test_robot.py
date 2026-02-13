from robot import Robot


def main():
    robot_id = input("Enter Robot ID: ")
    start_location = input("Enter starting location (ex: A3): ")

    robot = Robot(robot_id, False, start_location)

    while True:
        print("\nCurrent Robot State:")
        print(robot)

        print("\nChoose an action:")
        print("1 - Turn ON")
        print("2 - Turn OFF")
        print("3 - Toggle Status")
        print("4 - Move Robot")
        print("5 - Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            robot.turnOn()

        elif choice == "2":
            robot.turnOff()

        elif choice == "3":
            robot.toggleStatus()

        elif choice == "4":
            new_loc = input("Enter new location: ")
            robot.moveBot(new_loc)

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid selection. Try again.")


if __name__ == "__main__":
    main()

