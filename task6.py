#!/usr/bin/python
import sys
import os
import json
import yaml

print("Version's Python is ", str(sys.version_info[0]) + "." + str(sys.version_info[1]) + "." + str(sys.version_info[2]))
vp = str(sys.version_info[0]) + "." + str(sys.version_info[1]) + "." + str(sys.version_info[2])

print ("Virtual Environment:")
os.system("pyenv virtualenvs")

print("Python Executable Location ", sys.executable)

print("Pip Location:")
os.system("which pip")

print ("PYTHONPATH:")
print(str((os.environ['PATH'].split(os.pathsep))[0]))

print ("Installed Packages: Name, Version:")
os.system("pip list")

i = 0
while i < len(sys.path):
	if 'site-packages' in sys.path[i]:
		print("Site-Packages Location ")
		print(sys.path[i])
	i += 1

def write_to_json():
	d1={}
	d1["Version"]=vp
	os.system("pyenv virtualenvs > specilFile.txt")
	f = open("specilFile.txt", 'r')
	content = f.read()
	f.close()
	d1["VE"]=content
	d1["PEL"]=sys.executable
	os.system("which pip > specilFile.txt")
	f = open("specilFile.txt", 'r')
	content = f.read()
	f.close()
	d1["Pip Location"]=content
	d1["PYTHONPATH"]=str((os.environ['PATH'].split(os.pathsep))[0])
	os.system("pip list > specilFile.txt")
	f = open("specilFile.txt", 'r')
	content = f.read()
	f.close()
	d1["Installed Packages"]=content

	i = 0
	while i < len(sys.path):
		if 'site-packages' in sys.path[i]:
			d1["Site-Packages Location "]=sys.path[i]
			print(sys.path[i])
		i += 1
		
	# open json file task6.json & write in it
	with open('task6.json', 'a') as myfile: 
		json.dump(d1, myfile, indent = 4, ensure_ascii = False)

def write_to_yaml():
	d1={}
	d1["Version"]=vp
	os.system("pyenv virtualenvs > specilFile.txt")
	f = open("specilFile.txt", 'r')
	content = f.read()
	f.close()
	d1["VE"]=content
	d1["PEL"]=sys.executable
	os.system("which pip > specilFile.txt")
	f = open("specilFile.txt", 'r')
	content = f.read()
	f.close()
	d1["Pip Location"]=content
	d1["PYTHONPATH"]=str((os.environ['PATH'].split(os.pathsep))[0])
	os.system("pip list > specilFile.txt")
	f = open("specilFile.txt", 'r')
	content = f.read()
	f.close()
	d1["Installed Packages"]=content
	i = 0
	while i < len(sys.path):
		if 'site-packages' in sys.path[i]:
			d1["Site-Packages Location "]=sys.path[i]
			print(sys.path[i])
		i += 1
		
	# open yaml file task6.yaml & write in it
	with open('task6.yaml', 'a') as myfile: 
		yaml.dump(d1, myfile, default_flow_style=False, allow_unicode=True)

write_to_json()
write_to_yaml()