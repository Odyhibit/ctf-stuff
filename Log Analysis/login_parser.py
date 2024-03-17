from log_utilities import *
from collections import defaultdict

username_logins = defaultdict(int)  # username: count
date_logins = defaultdict(int)      # date: count
username_ips = defaultdict(set)     # username: (ip1, ip2, ...)

with open("Login/login.log", "r") as log_file:
    for i, line in enumerate(log_file):
        line = ' '.join(line.split())  # combines multiple spaces into one
        date, time, ip, *user = line.split()
        user = " ".join(user)

        username_logins[user] += 1
        date_logins[date] += 1
        username_ips[user].add(ip)

print(f"Q1 {in_green(i + 1)} login attempts")
print(f"Q3 {in_green(len(username_logins))} unique usernames")
print(f"Q3 {in_green(max(username_logins, key=username_logins.get))} has the most login attempts")
print(f"Q4 {in_green(username_logins[max(username_logins, key=username_logins.get)])} attempts")
print(f"Q5 {in_green(max(date_logins, key=date_logins.get))} had the most attempts")
print(f"Q6 {in_green(get_key_with_longest_set(username_ips))} ")

"""
Q1 How many total login attempts were made in this log?
Q2 How many unique usernames appear in this log?
Q3 What is the username with the most login attempts?
Q4 How many attempts were made for the username with the most login attempts?
Q5 What is the date with the most login attempts?
Q6 What is the username that had logins from the most unique IP addresses?
"""