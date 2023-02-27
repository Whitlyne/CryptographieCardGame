## Projet de Cryptographie 

Projet de Cryptographie en deuxième semestre de M1 BDIA .

### Comment lancer le projet

#### Nécessaire 

Python 3 dans être installer sur votre ordinateur

#### Interface visuelle
Pour un lancement avec une interface visuelle : 

Sous linux vous devez installer une librairie pour l'affichage : 

```sh 
sudo apt-get install python3-pil python3-pil.imagetk
```

ou de lancer le makefile : 

```sh 
make install 
```

Ensuite lancer l'interface graphique :

```sh
python3 ProjetCryptographie.py
```

#### Interface console

Il faut se déplacer dans le dossier srcwithoutgui puis lancer la commande : 

```sh 
python3 CryptageWithoutGUI.py "fichier.txt a décrypter"
```

Pour lancer le décryptage : 

```sh 
python3 CryptageWithoutGUI.py "fichier.txt à decrypted" "le deck au format txt"
```


