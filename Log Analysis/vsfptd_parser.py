from log_utilities import *

with open("VSFPTD/vsftpd.log", "r") as log_file:
    upload = 0
    other_upload = 0
    download = 0
    ips = set()
    users = set()

    for line in log_file:
        ips.add(get_text_between(line, 'Client "', '"'))
        users.add(line.split()[7])
        if " bytes," in line:

            end = line.find(" bytes,")
            start = line.rfind(" ", 0, end)
            num_bytes = int(line[start:end])
            if "[ftpuser]" in line and "UPLOAD:" in line:
                upload += num_bytes
            if "[ftpuser]" not in line and "UPLOAD:" in line:
                other_upload += num_bytes
            if "[ftpuser]" in line and "DOWNLOAD:" in line:
                download += num_bytes

    print(f"Users {users}")
    print(f"Other user bytes uploaded {other_upload}")
    print(f"{in_green(upload)} bytes uploaded")
    print(f"{in_green(download)} bytes downloaded")
    print(ips)

"""
Q1 What IP address did "ftpuser" first log in from?
    10.0.0.123
Q2 What is the first directory that ftpuser created?
    /home/ftpuser/TreeSizeFree
Q3 What is the last directory that ftpuser created?
    /home/ftpuser/110D300S
Q4 What file extension was the most used by ftpuser?
    .JPG
Q5 What is the username of the other user in this log?
    jimmy
Q6 What IP address did this other user log in from?
    10.0.0.214
Q7 How many total bytes did this other user upload?
    105750628
Q8 How many total bytes did ftpuser upload?
    13980839165
Q9 How many total bytes did ftpuser download?
    6008032
Q10 Identify the suspicious (login with no activity) login IP address in this log.
    10.3.0.6
"""