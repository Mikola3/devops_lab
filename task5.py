#!/usr/bin/python
# import json
import requests
import argparse
# from datetime import datetime

# parsing
parser = argparse.ArgumentParser()
parser.add_argument("-r", "--repos", help="GH's repository", action="store_true")
parser.add_argument("-v", "--version", help="Script's version", action="store_true")
parser.add_argument("-l", "--label", help="GH's label", action="store_true")
parser.add_argument("--ref", help="GH's ref", action="store_true")
parser.add_argument("-i", "--id", help="GH's id", action="store_true")
parser.add_argument("-p", "--pushtime", help="Push Time", action="store_true")

# set variables
p = parser.parse_args()

u = input("Please, Enter Github's User: ")
r = "alenaPy/devops_lab"

# auth. on Github
import getpass
pwd = getpass.getpass(prompt="Please, Enter Your Password: ")

print(u)
print(r)
url = "https://api.github.com/repos/" + str(r) + "/" + "pulls"
# print(url)
reqget = requests.get(url, auth=(u, pwd))
reqjson = reqget.json()
# print(json.dumps(reqjson, sort_keys=True, indent=4, ensure_ascii=False))

# check input parameters
if p.version:
    print("Programm's version is script_1.0")
elif p.repos:
    print(reqjson[0].get("base").get("repo").get("name"))
elif p.pushtime:
    limit = len(reqjson)
    for i in range(limit):
        L = reqjson[i].get("head").get("repo").get("pushed_at")
        DATE, TIME = L.split('T')
        print("Push Time is " + TIME[0:8:1])
elif p.label:
    limit = len(reqjson)
    for i in range(limit):
        print("Label's name is " + reqjson[i].get("head").get("label"))
elif p.ref:
    limit = len(reqjson)
    for i in range(limit):
        print("Ref is " + reqjson[i].get("head").get("ref"))
elif p.id:
    limit = len(reqjson)
    for i in range(limit):
        print("Id is " + str(reqjson[i].get("user").get("id")))
else:
    print("Please, Enter the Correct Key")
