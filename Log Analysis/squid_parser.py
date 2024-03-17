from log_utilities import *

year = ""
request_times = []
ips = set()
get_requests = 0
post_requests = 0
anti_virus = ""

with open("./Squid/squid_access.log", "r") as log_file:
    for line in log_file:
        timestamp, processing_time, client_ip, cache_result, num_bytes, \
            request_method, url, user, route, response_type = line.split()
        processing_time = int(processing_time)
        year = timestamp_to_year(timestamp)
        request_times.append(processing_time)
        ips.add(client_ip)
        if request_method == "GET":
            get_requests += 1
        if request_method == "POST":
            post_requests += 1
        if "192.168.0.224" in client_ip:
            anti_virus = url

print(f"Q1 log was in {in_green(year)}")
print(f"Q2 fastest time was {in_green(min(request_times))}")
print(f"Q3 longest request was {in_green(max(request_times))}")
print(f"Q4 there are {in_green(len(ips))} ips")
print(f"Q5 there are {in_green(get_requests)} GET requests")
print(f"Q6 there are {in_green(post_requests)} POST requests ")
print(f"Q7 ani-virus company url is {in_green('Symantec')}")  # found by hand ctl+f 'virus'
print(f"Q8 update url is {in_green(anti_virus)}")

""""
Q1 In what year was this log saved?
Q2 How many milliseconds did the fastest request take?
Q3 How many milliseconds did the longest request take?
Q4 How many different IP addresses did the proxy service in this log?
Q5 How many GET requests were made?
Q6 How many POST requests were made?
Q7 What company created the antivirus used on the host at 192.168.0.224?
Q8 What url is used to download an antivirus update?
"""
