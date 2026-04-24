import time
import sys
import os

def main():
    possible_paths = [
        '/home/pi/project_demo/lib',
        '/home/yahboom/project_demo/lib',
    ]

    for path in possible_paths:
        if os.path.exists(path):
            sys.path.append(path)

    from Raspbot_Lib import Raspbot

    bot = Raspbot()

    def stop_all():
        for i in range(4):
            bot.Ctrl_Muto(i, 0)

    def set_all(m1, m2, m3, m4):
        bot.Ctrl_Muto(0, int(m1))
        bot.Ctrl_Muto(1, int(m2))
        bot.Ctrl_Muto(2, int(m3))
        bot.Ctrl_Muto(3, int(m4))

    try:
        print("Testing each motor individually...")
        for motor in range(4):
            print(f"Motor {motor} forward")
            bot.Ctrl_Muto(motor, 40)
            time.sleep(1)
            bot.Ctrl_Muto(motor, 0)
            time.sleep(0.5)

        print("Testing all motors forward...")
        set_all(40, 40, 40, 40)
        time.sleep(1)
        stop_all()
        time.sleep(1)

        print("Testing all motors backward...")
        set_all(-40, -40, -40, -40)
        time.sleep(1)
        stop_all()
        time.sleep(1)

        print("Testing rotate left...")
        set_all(-40, -40, 40, 40)
        time.sleep(1)
        stop_all()
        time.sleep(1)

        print("Testing rotate right...")
        set_all(40, 40, -40, -40)
        time.sleep(1)
        stop_all()

        print("Motor test complete.")

    except KeyboardInterrupt:
        print("Interrupted. Stopping motors.")
        stop_all()

    finally:
        stop_all()


if __name__ == '__main__':
    main()
