from tkinter import *
import random
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

# Variable
deck = []
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
cryptAlphabet = {}
texttodecode = ''
clef = []
iration = 0

root = Tk()
root.title('Crypto - Message a coder')
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
	root.title('CryptoProjet')
	root.update() 

# Evaluate the value to the card give in parameter
def evaluatCard(card):
	if(card == "jokerblack"):
		valueCard = 53
	elif(card == "jokerred"):
		valueCard = 54
	else:
		suits = {"clubs": 1, "diamonds": 2, "hearts": 3, "spades": 4}
		infoCard = card.split("_")
		valueCard = int(infoCard[0]) * int(suits[infoCard[1]])
	return valueCard

# Choose file
def chooseFile():
    global texttodecode
    fileToCrypt = askopenfilename(parent=root, title="Ouvrir votre document", filetypes=[('txt files', '.txt')])
    with open(fileToCrypt) as file:
        texttodecode=file.readlines()

    texttodecodetemp = []
    for text in texttodecode:
		# Suppression des espaces
        textSplit = text.replace(" ", "")
		# Suppression des retours chariots
        textSplit = textSplit.replace("\n", "")
        # Mise en minuscule de la chaine de caractere
        textSplit = textSplit.lower()
        texttodecodetemp.append(textSplit)

    texttodecode.clear()
    texttodecode = texttodecodetemp
    print(texttodecode)


def write_array_to_file(array, filename):
    with open(filename, 'w') as file:
        for item in array:
            file.write(str(item) + '\n')
    print(f"Tableau écrit dans le fichier '{filename}'.")

# Operation 1
def operation1():
	jokerblack = deck.index("jokerblack")
	if jokerblack == 53 :
		deck[53]=deck[1]
		deck[1] = "jokerblack"	
	else :
		deck[jokerblack]=deck[jokerblack+1]
		deck[jokerblack+1] = "jokerblack"

# Operation 2
def operation2():
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

# Operation 3
def operation3():
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

# Operation 4
def operation4():
	global deck

	lastCard = deck[len(deck)-1]
	valueCard = 0
	if(lastCard == "jokerred" or lastCard == "jokerblack"):
		valueCard = 53
	else:
		valueCard = evaluatCard(lastCard)

	deckTemp1 = deck[0:valueCard]
	deckTemp2 = deck[valueCard:len(deck)-1]
	deck.clear()
	deck = deckTemp2 + deckTemp1
	deck.append(lastCard)

# Operation 5
def operation5():
	global deck
	firstCard = deck[0]
	valueFirstCard = evaluatCard(firstCard)
	valueCardPseudoAlea = -1

	# La carte à la position de la valeur de la première carte (firstCard)
	print("Valeur de la premiere carte : ", valueFirstCard)
	cardPseudoAlea = deck[valueFirstCard - 1]
	print(cardPseudoAlea)

	if(cardPseudoAlea == "jokerred" or cardPseudoAlea == "jokerblack"):
		operation1()
		operation2()
		operation3()
		operation4()
		# Operation5 se rappel elle meme jusqu'a ce que l'on trouve on valeur correcte, un peu comme une fonction récursive
		valueCardPseudoAlea = operation5()
	else:
		valueCardPseudoAlea = evaluatCard(cardPseudoAlea)
		if(valueCardPseudoAlea > 26):
			valueCardPseudoAlea = valueCardPseudoAlea - 26	
	
	print("Valeur de la carte pseudo aléa : ", valueCardPseudoAlea)
	return valueCardPseudoAlea

# Function to crypt the file
def encrypted(val):
	global texttodecode
	global clef
	global deck
	subClef = ""
	if(val == "True"):
		write_array_to_file(deck,"deckToSend.txt")
	#  Boucle pour parcourir tous les éléments de la liste 
	#  while len(clef) < totalLengOfListTextToDecode:
	for text in texttodecode:
		# Second boucle pour traiter chaque éléments de la liste 
		for element in text:
			print(element)
			operation1()
			operation2()
			operation3()
			operation4()
			subClef += alphabet[operation5() - 1]
		clef.append(subClef)
		subClef = ""

	printDeck()
	print(clef)
	cryptedMessage(clef,val)

# Fonction to addition value of alphabet and la valeur de la clé 
def cryptedMessage(clef,val):
	global texttodecode
	global iration
	global alphabet
	messagecrypted=[]
	ligne = ''
	if (val == "True"):
		for string1, string2 in zip(texttodecode, clef):
			for i in range(len(string1)) :
				tempo = (alphabet.index(string1[i]) + alphabet.index(string2[i]))
				if(tempo>25):
					tempo = tempo - 25 
				ligne +=alphabet[tempo]
			messagecrypted.append(ligne)
			ligne=""
		write_array_to_file(messagecrypted,'textCrypted.txt')
	else :
		for string1, string2 in zip(texttodecode, clef):
			for i in range(len(string1)) : 
				tempo = (alphabet.index(string1[i]) - alphabet.index(string2[i]))
				if(tempo < 0  ):
					tempo = tempo + 25 
				ligne +=alphabet[tempo]
			messagecrypted.append(ligne)
			ligne=""
		write_array_to_file(messagecrypted,'textDecrypted.txt')

def decryptage():
    global deck
    global texttodecode
    futurdeck = askopenfilename(parent=root, title="Ouvrir votre paquet de cartes", filetypes=[('txt files', '.txt')])
    with open(futurdeck) as file:
        deck=file.readlines()
    
    decktemp = []
    for text in deck:
		# Suppression des espaces
        textSplit = text.replace(" ", "")
		# Suppression des retours chariots
        textSplit = textSplit.replace("\n", "")
        # Mise en minuscule de la chaine de caractere
        textSplit = textSplit.lower()
        decktemp.append(textSplit)
    
    deck.clear()
    deck = decktemp
    print(deck)
    
    fileToCrypt = askopenfilename(parent=root, title="Ouvrir votre document", filetypes=[('txt files', '.txt')])
    with open(fileToCrypt) as file:
        texttodecode=file.readlines()
    
    texttodecodetemp = []
    for text in texttodecode:
		# Suppression des espaces
        textSplit = text.replace(" ", "")
		# Suppression des retours chariots
        textSplit = textSplit.replace("\n", "")
        # Mise en minuscule de la chaine de caractere
        textSplit = textSplit.lower()
        texttodecodetemp.append(textSplit)
    
    texttodecode.clear()
    texttodecode = texttodecodetemp
    print(texttodecode)
    
    encrypted("False")
    
# Step 1 for the deck
def step1():
	operation1()
	printDeck()

# Step 2 for the deck
def step2():
	operation2()
	printDeck()

# Step 3 for the deck
def step3():
	operation3()
	printDeck()

# Step 4 for the deck
def step4():
	operation4()
	printDeck()

# Step 5 for the deck
def step5():
	print(alphabet[operation5() - 1])
	printDeck()

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


# Button for choose the file to lauch encryptage
file_button = Button(root, text="Lancer l'encryptage", font=("Helvetica", 14), command=lambda : encrypted("True"))
file_button.pack(pady=20)

# Button for choose the file to lauch encryptage
file_button = Button(root, text="Lancer decryptage", font=("Helvetica", 14), command=decryptage)
file_button.pack(pady=20)


# Button for quit the app
quit_button = Button(root, text="Quitter", font=("Helvetica", 14), command=quit)
quit_button.pack(pady=20)

# Shuffle Deck On Start
shuffle()

root.mainloop() 


