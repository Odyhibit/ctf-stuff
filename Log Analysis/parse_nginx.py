from log_utilities import *

all_ips = set()
response_200 = 0
response_400 = 0
doorbell, googlebot, shellshock = "", "", ""
firefox = {}
request_type_dict = {}
request_hex = 0

with open("NginX/access.log", "r") as log_file:
    for line in log_file:
        ip = line.split(" ")[0]
        request = in_quotes(line)
        response_code = line.split('"')[2].strip().split(" ")[0]
        response = in_quotes(line, 2)
        useragent = in_quotes(line, 3)
        request_type = request.split(" ")[0]

        all_ips.add(ip)
        if response_code == "200":
            response_200 += 1
        if response_code == "400":
            response_400 += 1
        if "bell" in request:
            doorbell = ip
        if "ooglebot" in useragent:
            googlebot = useragent
        if "bash -c" in response:
            shellshock = ip
        if "irefox" in useragent:
            add_or_create(firefox, useragent)
        add_or_create(request_type_dict, request_type)
        if "\\x04\\x01\\x00P\\xC6\\xCE\\x0Eu0\\x00" in request:
            request_hex += 1

sorted_request_type_dict = sorted(request_type_dict, key=request_type_dict.get, reverse=True)
print(f"Q1 There are {in_green(len(all_ips))} addresses")
print(f"Q2 There are {in_green(response_200)} 200 responses")
print(f"Q3 There are {in_green(response_400)} 400 responses")
print(f"Q4 IP address {in_green(doorbell)} rang the doorbell")
print(f"Q5 google bot version {in_green(googlebot.split(';')[1])}")
print(f"Q6 {in_green(shellshock)} tried to use shellshock")
print(f"Q7 Most popular version of firefox is {in_green(max(firefox, key=firefox.get).split(' ')[6])}")
print(f"Q8 most common request type is {in_green(sorted_request_type_dict[0])}")
print(f"Q9 second most common request type is {in_green(sorted_request_type_dict[1])}")
print(f"Q10 \\x04\\x01\\x00P\\xC6\\xCE\\x0Eu0\\x00 was requested {in_green(request_hex)} times")

"""
Q1 How many different IP addresses reached the server?
Q2 How many requests yielded a 200 status?
Q3 How many requests yielded a 400 status?
Q4 What IP address rang at the doorbell?
Q5 What version of the Googlebot visited the website?
Q6 Which IP address attempted to exploit the shellshock vulnerability?
Q7 What was the most popular version of Firefox used for browsing the website?
Q8 What is the most common HTTP method used?
Q9 What is the second most common HTTP method used?
Q10 How many requests were for \x04\x01\x00P\xC6\xCE\x0Eu0\x00?
"""