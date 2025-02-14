#!/usr/bin/python3
while True:
	text = input("Prompt:~$ ").lower().strip()
	if text == "quit" or text == "exit":
		break
	elif text == "pass":
		continue
	else:
		print(text)
