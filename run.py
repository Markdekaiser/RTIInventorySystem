import subprocess
import sys
import pip
import socket

def install(django):
    pip.main(['install', django])

def isDjangoInstalled():
    try:
        import django
        return True
    except ImportError:
        print ('django is not installed, installing it now!')
        install('django')
        return False

from sys import platform
if platform == "linux" or platform == "linux2":
    if isDjangoInstalled():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        print(f"Ip Address: {ip}")
        subprocess.run(["python","manage.py","runserver",ip + ":8000"])
    else:
        print('Please rerun this file')
        sys.exit(1)


elif platform == "win32":
    if isDjangoInstalled():
        hostname = socket.getfqdn()
        #hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(f"Hostname: {hostname}")
        print(f"IP Address: {ip_address}")
        subprocess.run(["python","manage.py","runserver",ip_address + ":8000"])
    else:
        print('Please rerun this file')
        sys.exit(1)


