import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/yahboom/Desktop/S26_RobotProgramming_Crystal/lab6/Ferrara/lab/roscourse_sim_ws/install/my_robot'
