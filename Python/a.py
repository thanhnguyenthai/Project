from random import randint

print("Nhap Dam, La, Keo:")
player = input()
computer = randint (0,2)


if computer == 0:
	computer = "Dam"
if computer ==1 :
	computer == "La"
if computer == 2:
	computer = "Keo"


print("---")
print("you choose:" + player.upper())
print("computer choose:" + computer.upper())
print("---")


if player == computer:
	print("DRAW")
else:
	if player == "DAM":
		if computer == "KEO":
			print("You Win")
		else:
			print("You Lose")

	elif player == "LA":
		if computer == "KEO":
			print("You Lose")
		else:
			print("You Win")

	elif player == "KEO":
		if computer == "DAM":
			print("You Lose")
		else:
			print("You Win")	

	else:
		print("Nhap Sai, Vui long nhap lai:")
