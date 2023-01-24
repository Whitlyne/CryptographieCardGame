from tkinter import *
import random
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk


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
	deck = []

	# Create the new deck
	# while (deck.__len__() < 55): 
	# 	card = random.randint(1,54)
	# 	if card not in deck:
	# 		deck.append(card)

	# print(deck)

	# Define Our Deck
	suits = ["diamonds", "clubs", "hearts", "spades"]
	values = range(1, 14)
	# 11 = Jack, 12=Queen, 13=King

	for suit in suits:
		for value in values:
			deck.append(f'{value}{suit}')

	deck.append('jokerblack')
	deck.append('jokerred')

	random.shuffle(deck)

	print(deck)

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

my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

# Button for shuffle the deck
shuffle_button = Button(root, text="Melanger le jeux de carte", font=("Helvetica", 14), command=shuffle)
shuffle_button.pack(pady=20)


# Button for choose the file to crypte
shuffle_button = Button(root, text="Choisir le fichier à crypter", font=("Helvetica", 14), command=chooseFile)
shuffle_button.pack(pady=20)


# Button for quit the app
shuffle_button = Button(root, text="Quitter", font=("Helvetica", 14), command=quit)
shuffle_button.pack(pady=20)

# Shuffle Deck On Start
shuffle()

root.mainloop() 