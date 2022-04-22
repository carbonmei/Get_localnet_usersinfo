#!python
"""
Script to set Static IP to the WiFi adaptor of laptop.
 so that it belongs to the same network address range
  as that of the WAP of the router configured to work like a switch.
"""
import subprocess
staticIP = '''netsh interface ip set address name="wifi" static 10.43.79.17 255.255.240.0 10.41.32.1'''
command1 = staticIP.split()
subprocess.run(command1)

staticDNS1 = '''netsh interface ip set dns name="wifi" static 221.5.88.88'''
command2 = staticDNS1.split()
subprocess.run(command2)

staticDNS2 = '''netsh interface ip add dns name="wifi" 116.116.116.116 index=2'''
command3 = staticDNS2.split()
subprocess.run(command3)