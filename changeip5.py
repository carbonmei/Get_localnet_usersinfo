"""
以下是如何恢复为自动获取 IP 地址（通过 DHCP）：
"""
import wmi
# Obtain network adaptors configurations
nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

# First network adaptor
nic = nic_configs[0]

# Enable DHCP
nic.EnableDHCP()