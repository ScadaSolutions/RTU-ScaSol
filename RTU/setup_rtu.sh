#!/bin/bash

echo "Sit back, this may take a while."
echo ""


sudo apt update
sudo apt install python3-pip
sudo apt-get install git-all
sudo apt-get install cmake


echo ""
echo "Almost Done..."
echo ""

sudo pip3 install adafruit-blinka
sudo pip3 install adafruit-circuitpython-mcp3xxx
sudo pip3 install multiprocess

echo ""
echo "Done! Enjoy ;)"
echo ""
