# [HARDWARE]
robot = True
eeg_live = True
eda_live = True

"""
to check available ports run the following code:
from serial.tools import list_ports

available_ports = list_ports.comports()
print(f'available ports: {[x.device for x in available_ports]}')

may need 
sudo chmod 666 /dev/ttyACM0
"""

# [DOBOT]
robot1_port = 'COM4' # '/dev/ttyACM0' or 'COM4' or 'COM10' or arm = XArmAPI('192.168.1.222')
robot2_port = '/dev/ttyXXXX'
robot_verbose = False

x_extents = [160, 350]
y_extents = [-150, 150]
z_extents = [0, 150]
irregular_shape_extents = 50

# [XARM]
xarm1_port = '192.168.1.222'
xarm2_port = '192.168.1.223'

xarm_x_extents = [160, 350]
xarm_y_extents = [-150, 150]
xarm_z_extents = [0, 150]
xarm_irregular_shape_extents = 50

# play params
silence_listener = False
duration_of_piece = 360
continuous_line = False
speed = 5
staves = 0
temperature = 0

# [BITALINO]
baudrate = 10
channels = [0]
mac_address = "98:D3:B1:FD:3D:1F"  #  "/dev/cu.BITalino-3F-AE"

# [DEBUG]
# debug = logging.INFO

# [STAFF]
staff_width = 20

# [STREAMING]
stream_list = [#'mic_in',
               'rnd_poetry',
               'eeg2flow',
               'flow2core',
               'core2flow',
               'audio2core',
               'audio2flow',
               'flow2audio',
               'eda2flow']
