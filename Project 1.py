"""
Implement a program that will launch a specified process and periodically (with a provided time interval) collect the
following data about it:
    • CPU usage (percent);
    • Memory consumption: Working Set and Private Bytes (for Windows systems) or Resident Set Size and Virtual Memory Size (for Linux systems);
    • Number of open handles (for Windows systems) or file descriptors (for Linux systems).
Data collection should be performed all the time the process is running. Path to the executable file for the process
and time interval between data collection iterations should be provided by user. Collected data should be stored on the
disk. Format of stored data should support automated parsing to potentially allow, for example, drawing of charts.
"""

import psutil
import csv
import os
from time import time, sleep
import resource
def create_csv(filename):

    headerList = ['CPU', 'RSS[Gb]', 'VMS[Gb]']
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            wd = csv.DictWriter(file, delimiter = ',', fieldnames=headerList)
            wd.writeheader()
    while True:
        sleep(timer - time() % 1)
        collect_log(filename)

def collect_log(filename):
    print("I'm here")
    cpu_usage = psutil.cpu_percent(0.1)
    rss = round((psutil.Process().memory_info().rss / (1024 * 1024)), 2)
    vms = round(((psutil.virtual_memory().used)/1000000000), 2)
    data = [cpu_usage, rss, vms]
    print(data)
    with open(filename, 'a') as f:
        f.write(",".join(map(str, data)))
        f.write("\n")
    create_csv(filename)

timer = float(input("Put interval: "))
create_csv('Data.csv')