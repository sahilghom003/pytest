import paramiko
import pytest
import psutil
import datetime

command = "ls"

host = "192.168.1.2"
username = "gslab"
password = "gslab2022"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
memory = psutil.virtual_memory()[2]
cpu_usage = psutil.cpu_percent(1)
_stdin, _stdout, _stderr = client.exec_command(command)
print(_stdout.read().decode())
client.close()
