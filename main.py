# Kana game version 0.1 =^_^=

from random import shuffle

def play(range): 

	#choice = input("On how many itens would you like to be tested? ")
	#choice = int(choice)

	if range <= 0 or range > 46: range = 10

	print("Starting game... \n")

	shuffle(kana)
	score = 0

	for i in kana[0:range]:
		print('', i)
		answer = input(' ')
		if answer == jisho[i]:
			score += 1
			print("Right!")
		else:
			print("Nope...")

	print("\nGame end, your score is: ", score, "!")
	if score == range: print("You nailed it!")
	
	choice = input("Type 1 if you want to play again: ")
	if choice is "1": play(range)
	else:
		print("Bye!")
		exit()

if __name__ == '__main__':

	print("\nWelcome to the Kana game, made in Python! (っ・ω・)っ",
			"\nWe have two versions:",
			"\n1 - Hiragana",
			"\n2 - Katakana")

	choice = input("Type the number you want to play: ")

	if choice == "1":
		fo = open("lists/hira.txt", "r")
		print("You chose Hiragana, have fun!")
	elif choice == "2":
		fo = open("lists/kata.txt", "r")
		print("You chose Katakana, have fun!")
	else:
		exit()

	# For later implementation maybe
	# choice != "1" or choice != "2":
	#	choice = input(" Please choose 1 or 2: ")

	for line in fo:
		kana = fo.read().splitlines()

	fo = open("lists/romaji.txt", "r")
	for line in fo:
		romaji = fo.read().splitlines()

	jisho = dict(zip(kana, romaji))

	range = input("On how many items would you like to be tested? ")
	range = int(range)

	play(range)







