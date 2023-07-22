import random 
from random import randint

Red = [32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3]
Black = [15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26]

while 1==1:
	Move_list = ["black","red"]

	Move = input("Black or Red")

	if Move.lower() in Move_list:
		Wheel = int(random.randint(0,36))

		if Move.lower() == "red":
			if Wheel in Red:
				print("Win", Wheel)
			else:
				print("Lose", Wheel)

		elif Move.lower() == "black":
			if Wheel in Black:
				print("Win", Wheel)
			else:
				print("Lose", Wheel)			
		
	elif Move.lower() == "end":
		break

	else:
		print("Input not accepted")
		pass

