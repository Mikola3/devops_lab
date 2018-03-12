#!/usr/bin/python
import psutil
import json
import time
from datetime import datetime
import myconf


class snapshot(object):
    def __init__(self):
        self.cput = None
        self.cpup = None
        self.vm = None
        self.sw = None
        self.diskp = None
        self.disku = None
        self.netc = None
        self.netint = None
        self.counter = 0
        self.time = None

    def meaning(self):
        self.cput = psutil.cpu_times()
        self.cpup = psutil.cpu_percent(interval=1)
        self.vm = psutil.virtual_memory()
        self.sw = psutil.swap_memory()
        self.diskp = psutil.disk_partitions()
        self.disku = psutil.disk_usage('/')
        self.netc = psutil.net_connections()
        self.netint = psutil.net_if_addrs()
        self.time = str(datetime.now())
        self.counter += 1

    def write_to_txt(self):
        f = open('system_info.txt', 'a')
        f.write(
            "SNAPSHOT "
            + str(self.counter)
            + " " + str(self.time)
            + "\n" + "1. CPU times"
            + "\n" + str(self.cput)
            + "\n\n"
        )
        f.write("2. CPU percent" + "\n" + str(self.cpup) + "\n\n")
        f.write("1. Virtual Memory" + "\n" + str(self.vm) + "\n\n")
        f.write("2. Swap Memory" + "\n" + str(self.sw) + "\n\n")
        f.write("1. Disk Partitions" + "\n" + str(self.diskp) + "\n\n")
        f.write("2. Disk Usage" + "\n" + str(self.disku) + "\n\n")
        f.write("1. Network connections" + "\n" + str(self.netc) + "\n\n")
        f.write("2. Network Interfaces" + "\n" + str(self.netint) + "\n\n")
        f.close()

    def write_to_json(self):
        d1 = {}
        d1["1. CPU times"] = self.cput
        d1["2. CPU percent"] = self.cpup

        d1["1. Virtual Memory"] = self.vm
        d1["2. Swap Memory"] = self.sw

        d1["1. Disk Partitions"] = self.diskp
        d1["2. Disk Usage"] = self.disku

        d1["1. Network connections"] = self.netc
        d1["2. Network Interfaces"] = self.netint
        # open json file system_info.json & write in it
        with open('system_info.json', 'a') as myfile:
            json.dump(d1, myfile, indent=4, ensure_ascii=False)


test = snapshot()
test.write_to_txt()
test.write_to_json()

while True:
    test.meaning()
    if myconf.output == "txt":
        test.write_to_txt()
    else:
        test.write_to_json()
    time.sleep(myconf.interval*60)
