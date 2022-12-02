from datetime import date, datetime
import speech_recognition
import pyttsx3

robot_mouth = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()
robot_brain=""

while True:
	with speech_recognition.Microphone() as mic:
		print("Robot: I'm listening")
		audio = robot_ear.listen(mic)

	print("Robot...")
	try:
		you = robot_ear.recognize_google(audio)
	except:
		you = "Can you say again?"
	print("You: " + you)




	if you == "":
		robot_brain = "I can't hear you, try again"
	elif "hello" in you:
		robot_brain = "Hello! How can i help you?"
	elif "today" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
	elif  "time" in you:
		now = datetime.now()
		robot_brain = now.strftime("%H hours %M minutes %S seconds")
	elif "handsome" in you:
		robot_brain = " It is you "
	elif "how are you" in you:
		robot_brain = " im fine thank you and you?"
	elif "bye" in you:
		robot_brain= "Bye"
		print(robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	else:
		robot_brain="Can  you say again? "

	print(robot_brain)
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()




	

