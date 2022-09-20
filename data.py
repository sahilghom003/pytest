import paramiko


def connect_host():
    host = "192.168.29.81"
    username = "gslab"
    password = "gslab2022"

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username, password)

    stdout = ssh.exec_command('python3 /home/pi/Documents/data_remote_check.py')[1]


connect_host()
