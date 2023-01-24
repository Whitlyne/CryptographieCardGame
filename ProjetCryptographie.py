from tkinter import *
import random
from PIL import Image, ImageTk


root = Tk()
root.title('Codemy.com - Card Deck')
# root.iconbitmap('c:/gui/codemy.ico')
root.geometry("900x500")
root.configure(background="green")

# Resize Cards
def resize_cards(card):
	# Open the image
	our_card_img = Image.open(card)

	# Resize The Image
	our_card_resize_image = our_card_img.resize((150, 218))
	
	# output the card
	global our_card_image
	our_card_image = ImageTk.PhotoImage(our_card_resize_image)

	# Return that card
	return our_card_image

# Shuffle The Cards
def shuffle():
	global deck
	deck = []

	# Create the new deck
	while (deck.__len__() < 55): 
		card = random.randint(1,54)
		# if card is not deck:
		if card not in deck:
			deck.append(card)

	print(deck)

	# Define Our Deck
	suits = ["diamonds", "clubs", "hearts", "spades"]
	values = range(1, 14)
	# 11 = Jack, 12=Queen, 13=King

	# for suit in suits:
	# 	for value in values:
	# 		deck.append(f'{value}_of_{suit}')

	# Create our players
	global player
	player = []

	# Grab a random Card For Dealer
	# card = random.choice(deck)
	# Remove Card From Deck
	# deck.remove(card)

	# Grab a random Card For Player
	# card = random.choice(deck)
	# Remove Card From Deck
	# deck.remove(card)
	# Append Card To Dealer List
	# player.append(card)
	# Output Card To Screen
	global player_image
	player_image = resize_cards(f'src/images/{card}.png')
	player_label.config(image=player_image)

	#player_label.config(text=card)

	# Put number of remaining cards in title bar
	root.title(f'Codemy.com - {len(deck)} Cards Left')


my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

player_frame = LabelFrame(my_frame, text="Player", bd=0)
player_frame.grid(row=0, column=1, ipadx=20)

player_label = Label(player_frame, text='')
player_label.pack(pady=20)


# Create a couple buttons
shuffle_button = Button(root, text="Melanger le jeux de carte", font=("Helvetica", 14), command=shuffle)
shuffle_button.pack(pady=20)


# Shuffle Deck On Start
# shuffle()

root.mainloop() 