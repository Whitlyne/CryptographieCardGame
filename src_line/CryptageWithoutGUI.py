import random
import sys

deck = []
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
    "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
cryptAlphabet = {}
texttodecode = ''
clef = []
iration = 0


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


def chooseFile():
    global texttodecode
    with open(sys.argv[1]) as file:
        texttodecode = file.readlines()

    texttodecodetemp = []
    for text in texttodecode:
        textSplit = ''.join(x for x in text if x.isalpha())
        textSplit = textSplit.lower()
        texttodecodetemp.append(textSplit)

    texttodecode.clear()
    texttodecode = texttodecodetemp
    print(texttodecode)


def chooseDeck():
	global deck
	with open(sys.argv[2]) as file:
		deck = file.readlines()
	decktemp = []
	for text in deck:
		textSplit = ''.join(x for x in text if x.isalpha())
		textSplit = textSplit.lower()
		decktemp.append(textSplit)
	deck.clear()
	deck = decktemp
	print(deck)

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
	global alphabet
	firstCard = deck[0]
	valueFirstCard = evaluatCard(firstCard)
	valueCardPseudoAlea = -1

	# La carte à la position de la valeur de la première carte (firstCard)
	print("Valeur de la premiere carte : ", valueFirstCard)
	cardPseudoAlea = deck[valueFirstCard - 1]
	print("Valeur de la carte a l'emplacement de la premire carte:",cardPseudoAlea)

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
	print("Lettre correspondante dans l'alphabet : ",alphabet[valueCardPseudoAlea - 1])
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
			operation1()
			operation2()
			operation3()
			operation4()
			subClef += alphabet[operation5() - 1]
		clef.append(subClef)
		subClef = ""
  
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


# Partie du main 

if(sys.argv.__len__() == 2):
    shuffle()
    chooseFile()
    encrypted("True")

if(sys.argv.__len__() == 3):
    chooseDeck()
    chooseFile()
    encrypted("False")