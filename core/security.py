import platform
import uuid
import subprocess
from functools import lru_cache


@lru_cache()
def get_computer_id() -> str:
    """
    获取计算机唯一标识
    Windows: 使用WMI获取主板序列号
    Linux: 使用dmidecode获取主板序列号
    如果获取失败则使用UUID作为备选方案
    """
    system = platform.system()

    try:
        if system == "Windows":
            # Windows下使用WMI获取主板序列号
            import wmi
            w = wmi.WMI()
            board = w.Win32_BaseBoard()[0]
            return board.SerialNumber.strip()

        elif system == "Linux":
            # Linux下使用dmidecode获取主板序列号
            cmd = "sudo dmidecode -s baseboard-serial-number"
            serial = subprocess.check_output(cmd.split()).decode().strip()
            return serial
        return str(uuid.uuid4())

    except Exception:
        # 如果获取失败,使用UUID作为备选
        return str(uuid.uuid4())