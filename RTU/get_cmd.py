import time
import os

with open("output.txt", "w") as initialized_file:
	initialized_file.close()

while True:
	cmd = input("RTU~$ ")
	with open("output.txt", "w") as out_file:
		out_file.write(cmd)
		out_file.close()
	time.sleep(0.7)
	with open("output.txt", "w") as out_file:
		out_file.write("")
		out_file.close()
	if cmd == "exit":
		os.remove("output.txt")
		break
