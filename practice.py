
import sys, getopt, os, shutil, json




name=" "
display_name=" "

if not name:
        name = input("Enter Name: ")
if not display_name:
        display_name = input("Enter display name: ")
if os.path.isdir(name):
    print("Action already exists with this name")
    sys.exit()
shutil.copytree(os.getcwd()+"/create_integration/source", os.getcwd()+"/create_integration/destination/"+name)