import base64
from log_utilities import *

all_ips = set()
daily_totals = {}
sent_ips = {}
with open("CustomFileFormat/Custom File Format.sky", "rb") as log:
    magic_bytes = log.read(8)
    version_number = log.read(1)
    creation_timestamp = log.read(4)
    hostname_len = bytes_to_int(log.read(4))
    hostname = log.read(hostname_len).decode("utf")
    flag_len = bytes_to_int(log.read(4))
    flag = log.read(flag_len)
    number_of_entries = bytes_to_int(log.read(4))

    for _ in range(number_of_entries):
        source = bytes_to_ip(log.read(4))
        destination = bytes_to_ip(log.read(4))
        date_time = bytes_to_date(log.read(4))
        num_bytes = int.from_bytes(log.read(4), "big")

        add_or_create(sent_ips, source, num_bytes)
        all_ips.add(source)
        all_ips.add(destination)
        add_or_create(daily_totals, date_time, num_bytes)

    print(f"Q1 the server-name is {in_green(hostname)}")
    print(f"Q2 the flag is {in_green(base64.b64decode(flag).decode('utf'))}")
    print(f"Q3 the file was created on {in_green(bytes_to_date(creation_timestamp))}")
    print(f"Q4 there are {in_green(number_of_entries)} entries in the log file.")
    print(f"Q5 there are {in_green(sum(sent_ips.values()))} bytes recorded in the log")
    print(f"Q6 there are {in_green(len(all_ips))} different IPs")
    print(f"Q7 {in_green(max(sent_ips, key=sent_ips.get))} sent the most data")
    print(f"Q8 {in_green(sent_ips[max(sent_ips, key=sent_ips.get)])} total bytes were sent")
    print(f"Q9 {in_green(max(daily_totals, key=daily_totals.get))} was the busiest day.")

"""
What is the hostname of the server?
What is the plaintext flag in the log file?
On what date was the file created (in UTC)?
How many entries are in the log file?
How many total transferred bytes were recorded in the log?
How many unique IP addresses (both senders and receivers) are recorded?
Which IP address sent the most amount of data?
How many total bytes were sent by the above IP address that sent the most amount of data?
What was the busiest day (day with the most bytes transferred)?
"""