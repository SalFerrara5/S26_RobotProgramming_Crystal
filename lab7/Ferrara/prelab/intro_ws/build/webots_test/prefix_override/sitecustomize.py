import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/yahboom/Desktop/S26_RobotProgramming_Crystal/lab7/Ferrara/prelab/intro_ws/install/webots_test'
