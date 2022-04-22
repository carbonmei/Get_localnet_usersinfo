"""您可以使用 Python WMI 模块来执行此操作（在运行这些脚本之前安装PyWin32 扩展和 WMI 模块）。以下是如何配置与硬件设备通信的方法："""

import wmi
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    pass# Code of your program here
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
# Obtain network adaptors configurations
nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

# First network adaptor
nic = nic_configs[0]

# IP address, subnetmask and gateway values should be unicode objects
ip = u'192.168.0.11'
subnetmask = u'255.255.255.0'
gateway = u'192.168.0.1'

# Set IP address, subnetmask and default gateway
# Note: EnableStatic() and SetGateways() methods require *lists* of values to be passed
nic.EnableStatic(IPAddress=[ip], SubnetMask=[subnetmask])
nic.SetGateways(DefaultIPGateway=[gateway])

