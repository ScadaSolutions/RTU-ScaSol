
Howdy! 

This is the ScaSol Capstone project from the class of 2023 that simulates a SCADA system.

Such system is compromised of one servo motor with feedback, a 
temperature sensor, a relay, and a switch. These components
simulate a real SCADA system but in a smaller and compact version. 

First step is to run: 'sudo ./setup-rtu.sh'.
This command installs all necessary libraries for the lab bench to 
function properly. 

The noly file necessary to start the RTU is 'main.py'. 

The swicth can be implemented to control the relay. To do so follow the steps below:

1.	'nano main.py'
2.	Add a '#' before the 3rd line of the file to comment the active multiprocess pool
3.	Remove '#' from the 4th line of the program to uncomment the inactive multiprocess
	pool

(Only one pool can be active at a time!)

ATTENTION!!!!
DO NOT CHANGE ANY DIRECTORY NAME OR FILES INSIDE '/RTU-Scasol/RTU/'!



