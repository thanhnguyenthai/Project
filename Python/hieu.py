you = "How are you"

if you == "":
	robot_brain = "I can't hear you, try again"
elif you == "Hello":
	robot_brain="Hello WINB"
elif you == "Today:":
	robot_brain="Thu 6"
else:
	robot_brain="I'm fine thank you. And you?"

print(robot_brain)