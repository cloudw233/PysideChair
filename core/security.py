import sys
import wmi
import subprocess

def get_computer_id():
    if sys.platform.startswith('win'):
        computer = wmi.WMI()
        cs = computer.Win32_ComputerSystem()[0]
        return cs.UUID
    elif sys.platform.startswith('linux'):
        output = subprocess.check_output(['dmidecode', '-s', 'system-uuid'])
        computer_id = output.decode().strip()
        return computer_id
    return None

