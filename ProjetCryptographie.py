from tkinter import *
import random
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

# Variable
deck = []

root = Tk()
root.title('Crypto - Paquet de cartes')
root.minsize(100, 200)
# root.attributes('-fullscreen', True)
# root.overrideredirect(True)
root.configure(background="green")

# Resize Cards
def resize_cards(card):
	# Open the image
	our_card_img = Image.open(card)

	# Resize The Image
	# original size
	# our_card_resize_image = our_card_img.resize((150, 218))
	# 60% of original size
	our_card_resize_image = our_card_img.resize((100, 145))
	# 30% of original size
	# our_card_resize_image = our_card_img.resize((50, 73))
	
	# output the card
	global our_card_image
	our_card_image = ImageTk.PhotoImage(our_card_resize_image)

	# Return that card
	return our_card_image

# Quit app
def quit():
	root.quit()

cards = []

# Shuffle The Cards
def shuffle():
	global deck
	deck.clear()

	# Create the new deck
	# while (deck.__len__() < 55): 
	# 	card = random.randint(1,54)
	# 	if card not in deck:
	# 		deck.append(card)

	# print(deck)

	# Define Our Deck
	suits = ["clubs", "diamonds", "hearts", "spades"]
	values = range(1, 14)
	# 11 = Jack, 12=Queen, 13=King

	for suit in suits:
		for value in values:
			deck.append(f'{value}_{suit}')

	deck.append('jokerblack')
	deck.append('jokerred')

	random.shuffle(deck)

	print(deck)
	printDeck()

# Print the deck
def printDeck():
	deck_frame = LabelFrame(my_frame, text="Les cartes", bd=0)
	deck_frame.grid(row=0, column=0)

	card_label_ = {}
	grid_column = 0
	grid_row = 0
	for card in deck:
		if (deck.index(card) % 18) == 0:
			grid_column = 0
			grid_row += 1

		imageCard = resize_cards(f'src/images/{card}.png')
		card_label_[card] = Label(deck_frame)
		card_label_[card].grid(column=grid_column, row=grid_row, ipady=4, ipadx=2)
		card_label_[card].config(image=imageCard)
		grid_column += 1
		cards.append(imageCard)

	# Put number of remaining cards in title bar
	root.title(f'Codemy.com - {len(deck)} Cards Left')
	root.update() 

# Choose file
def chooseFile():
	fileToCrypt = askopenfilename()

# Step 1 for the deck
def step1():
	fileToCrypt = askopenfilename()

# Step 2 for the deck
def step2():
	global deck
	jokerRed = deck.index("jokerred")

	# Cas 1 : on passe en position 3
	if(jokerRed == 53):
		deckTemp1 = deck[0:2]
		deckTemp2 = deck[2:jokerRed]
		deckTemp3 = ["jokerred"]
		deck.clear()
		deck = deckTemp1 + deckTemp3 + deckTemp2

	# Cas 2 : on passe en position 2
	elif(jokerRed == 52):
		deckTemp1 = deck[0:1]
		deckTemp2 = deck[1:jokerRed]
		deckTemp3 = ["jokerred"]
		deckTemp4 = deck[jokerRed+1:54]
		deck.clear()
		deck = deckTemp1 + deckTemp3 + deckTemp2 + deckTemp4

	# Cas 3 : on avance de 2 place
	else:
		deckTemp1 = deck[0:jokerRed]
		deckTemp2 = deck[jokerRed+1:jokerRed+3]
		deckTemp3 = ["jokerred"]
		deckTemp4 = deck[jokerRed+3:54]
		deck.clear()
		deck = deckTemp1 + deckTemp2 + deckTemp3 + deckTemp4

	printDeck()

# Step 3 for the deck
def step3():
	global deck
	
	# Search the position of the two jokers
	jokerBlack = deck.index("jokerblack")
	jokerRed = deck.index("jokerred")

	firstJoker = 0
	secondJoker = 0
	deckTemp4 = []
	deckTemp5 = []
	if(jokerRed < jokerBlack):
		firstJoker = jokerRed
		secondJoker = jokerBlack
		deckTemp4 = ["jokerred"]
		deckTemp5 = ["jokerblack"]
	else:
		firstJoker = jokerBlack
		secondJoker = jokerRed
		deckTemp4 = ["jokerblack"]
		deckTemp5 = ["jokerred"]

	deckTemp1 = deck[0:firstJoker]
	deckTemp2 = deck[firstJoker+1:secondJoker]
	deckTemp3 = deck[secondJoker+1:len(deck)]
	deck.clear()
	deck = deckTemp2 + deckTemp4 + deckTemp1 + deckTemp5 + deckTemp3 
	print(deck)
	printDeck()

# Step 4 for the deck
def step4():
	global deck

	suits = {"clubs": 1, "diamonds": 2, "hearts": 3, "spades": 4}
	values = range(1, 14)
	# 11 = Jack, 12=Queen, 13=King

	lastCard = deck[len(deck)-1]
	valueCard = 0
	if(lastCard == "jokerred" or lastCard == "jokerblack"):
		valueCard = 53
		print(valueCard)
	else:
		infoLastCard = lastCard.split("_")
		valueCard = int(infoLastCard[0]) * int(suits[infoLastCard[1]])
		print(infoLastCard[0])
		print(suits[infoLastCard[1]])
		print(valueCard)

	print(lastCard)

	printDeck()

# Step 5 for the deck
def step5():
	fileToCrypt = askopenfilename()

my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

# Button for shuffle the deck
shuffle_button = Button(root, text="Melanger le jeux de carte", font=("Helvetica", 14), command=shuffle)
shuffle_button.pack(pady=20)

# Buttons for differents step
test_frame = Frame(root, bg="blue")
test_frame.pack(pady=20)
step1_button = Button(test_frame, text="Etape 1", font=("Helvetica", 14), command=step1)
step1_button.pack(side=LEFT, ipady=4, ipadx=2)
step2_button = Button(test_frame, text="Etape 2", font=("Helvetica", 14), command=step2)
step2_button.pack(side=LEFT, ipady=4, ipadx=2)
step3_button = Button(test_frame, text="Etape 3", font=("Helvetica", 14), command=step3)
step3_button.pack(side=LEFT, ipady=4, ipadx=2)
step4_button = Button(test_frame, text="Etape 4", font=("Helvetica", 14), command=step4)
step4_button.pack(side=LEFT, ipady=4, ipadx=2)
step5_button = Button(test_frame, text="Etape 5", font=("Helvetica", 14), command=step5)
step5_button.pack(side=LEFT, ipady=4, ipadx=2)

# Button for choose the file to crypte
file_button = Button(root, text="Choisir le fichier à crypter", font=("Helvetica", 14), command=chooseFile)
file_button.pack(pady=20)


# Button for quit the app
quit_button = Button(root, text="Quitter", font=("Helvetica", 14), command=quit)
quit_button.pack(pady=20)

# Shuffle Deck On Start
shuffle()

root.mainloop() 