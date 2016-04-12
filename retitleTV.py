import os

import shutil

def goto_dir():

	print "\n\nPlease type the absolute directory of the shows you want to rename"
	place = raw_input("\n\n> ")
	os.chdir(place)
	newplace = os.getcwd()

def show_files():
	cwd = os.getcwd()
	print "\nHere is a list of the files in %s \n" % cwd
	contents = os.listdir(cwd)
	for i in contents:
		print i

goto_dir()
show_files()

org_files = os.listdir(os.getcwd())

extentions = []

for i in range(len(org_files)):
	x = org_files[i]
	y = x.split(".")
	z = y.pop()
	extentions.append(z)

print "\nEnter the name of the show:"
show_name = raw_input("\n> ")

print "\nEnter the season of the show: (i.e '02' or '12')"
season = raw_input("\n> ")

print "\nSo the episodes will be renamed like this:"
print "\n%s.S%sEXX.Title.of.Episode\n" % (show_name, season)
print "\n\nEnter the list of titles seperated by a semicolon: title of ep1;title of ep2;etc"
ep_titles = raw_input("\n\n> ")
ep_title_list = ep_titles.split(";")
print "\n\nThe file names will be changed as follows:"
first = ep_title_list[0]
print "\n\n" + org_files[0] + " ----> %s.S%sE01.%s." % (show_name, season, first) + extentions[i]

stop = raw_input("\n\n> ")

elements = []

print "\n\n Here is a list of how the files will look after the rename:"
print "\n"
for i in range(len(ep_title_list)):
	print "%s.S%sE" % (show_name, season) + str(i + 1).zfill(2) + '.' + ep_title_list[i] + "." + extentions[i]

stop = raw_input("\n\n> ")

for i in range(len(ep_title_list)):
	elements.append("%s.S%sE" % (show_name, season) + str(i + 1).zfill(2) + '.' + ep_title_list[i] + "." + extentions[i])
	
print "\n\n\nPress Enter to make the following changes:"
print "\n"

for i in range(len(elements)):
	print org_files[i] + " ------> " + elements[i]

stop = raw_input("\n\n\nReady?")

for i in range(len(ep_title_list)):
		org = org_files[i]
		new = elements[i]
		shutil.move(org, new)