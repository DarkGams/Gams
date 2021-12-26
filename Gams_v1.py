import socket 
from datetime import *
from random import *
from colorama import*
from pystyle import Anime, Colors, Colorate, Center, Box


print("""\n ██████╗  █████╗ ███╗   ███╗███████╗
██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██║  ███╗███████║██╔████╔██║███████╗
██║   ██║██╔══██║██║╚██╔╝██║╚════██║
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████║e
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                       Beta by Gam's         """)

print("==========================================")

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

print("Your computer is : " + hostname, "\nYour computer IP adress is : " + IP)

time = date.today()
print("Date : ", time)

print("==========================================")

choice = input("WELCOME TO Gam's Tool !\n\nWhat do you want to start ?\n\n1 > I want to play a game\n\n2 > I want to generate a password\n\n3 > I want to crypting a file")

def games():
	select = input("1 > Lounux By Gam's\n\n2 > Chifoumi By Gam's\n\n3 > Morpion By Gam's\n\nTapez ENTRER pour sortir")

	def Lounux():

		import random

		init()

		print(Fore.BLUE + """                   __                                    
		  / /    ___   _   _  _ __   _   _ __  __
		 / /    / _ \ | | | || '_ \ | | | |\ \/ /
		/ /___ | (_) || |_| || | | || |_| | >  < 
		\____/  \___/  \__,_||_| |_| \__,_|/_/\_\\
                                           """)

		print(Fore.GREEN + "Bienvenue sur Lounux , le jeu du Juste Prix !\nVous avez dix essais pour devinner un chiffre entre 0 à 100")

		trial = 0
		nb_trials = 10

		number = random.randint(0, 100)
		choice = int(input("Trouvez le juste prix : "))

		while True:
			if trial == nb_trials:
				print("Nombres d'essais dépassés")
				input("Apppuyez sur ENTRER pour quitter")
				break

			else:
				if choice == number:
					print("Félicitation , vous avez trouvé le juste prix !")
					print("Nombres d'essais : ", trial)
					input("Appuyez sur ENTRER pour quitter")
					break

				else:
					trial +=1
					if choice < number:
						print("C'est plus !")
						choice = int(input("Réessayez : "))

					else:
						print("C'est moins !")
						choice = int(input("Réessayez : "))

		retry = input("Do you want to play again ? Y/N")

		if retry == 'y':
			Lounux()

		elif retry != 'y':
			games()

	def chifoumi():
		
		print("""\n ██████╗██╗  ██╗██╗███████╗ ██████╗ ██╗   ██╗███╗   ███╗██╗
██╔════╝██║  ██║██║██╔════╝██╔═══██╗██║   ██║████╗ ████║██║
██║     ███████║██║█████╗  ██║   ██║██║   ██║██╔████╔██║██║
██║     ██╔══██║██║██╔══╝  ██║   ██║██║   ██║██║╚██╔╝██║██║
╚██████╗██║  ██║██║██║     ╚██████╔╝╚██████╔╝██║ ╚═╝ ██║██║
 ╚═════╝╚═╝  ╚═╝╚═╝╚═╝      ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝
                                                  By Gam's\n""")

		def game():

			print("Vous jouez a chifoumi contre l'ordi , il peut choisir 3 options , les voici :\n\n1-Pierre\n2-Feuille\n3-Ciseaux\n")

			choix_joueur = input('Pierre (p), Feuille (f) ou Ciseaux (c) ?')
			choix_pc = randint(1, 3)

			if choix_pc == 1:
				choix_pc == "Pierre"

			elif choix_pc == 2:
				choix_pc == "Feuille"

			elif choix_pc == 3:
				choix_pc == "Ciseaux"

			if choix_joueur == 'p':
				print("Vous avez choisi Pierre.")
				print("L'ordinateur a choisi", choix_pc)

			elif choix_joueur == 'f':
				print("Vous avez choisi Feuille.")
				print("L'ordinateur a choisi", choix_pc)

			elif choix_joueur == 'c':
				print("Vous avez choisi Ciseaux.")
				print("L'ordinateur a choisi", choix_pc)

			if (choix_joueur == 'p' and choix_pc == 3) or (choix_joueur == 'f' and choix_pc == 1) or (choix_joueur == 'c' and choix_pc == 2):
				print("Vous gagnez !")

			elif (choix_joueur == 'p' and choix_pc == 2) or (choix_joueur == 'f' and choix_pc == 3) or (choix_joueur == 'c' and choix_pc == 1):
				print("L'ordinateur gagne !")

			elif (choix_joueur == 'p' and choix_pc == 1) or (choix_joueur == 'f' and choix_pc == 2) or (choix_joueur == 'c' and choix_pc == 3):
				print("Egalité !")

			retry = input("\nVoulez vous rejouer ? O/N")

			if retry == 'o':
				game()
			elif retry != 'o':
				games()
				

		start = input("Appuyez sur une touche pour commencer")

		if start =='':
			game()


	def morpion():
		from tkinter import Tk, Canvas
		import random

		#gril
		game = [[0,1,2],[0,1,2],[0,1,2]]

		#GUIgrill
		def gril(c="black"):
			canvas.create_line((100,0),(100,300), width=3, fill=c)
			canvas.create_line((200,0),(200,300), width=3, fill=c)
			canvas.create_line((0,100),(300,100), width=3, fill=c)
			canvas.create_line((0,200),(300,200), width=3, fill=c)

		#pions
		def pions():
			for x in range(3):
				for y in range(3):
					xx = x * 100
					yy = y * 100
					A = (xx+20,yy+20)
					B = (xx+80,yy+80)
					C = (xx+20,yy+80)
					D = (xx+80,yy+20)
					if game[x][y] == 1:
						canvas.create_oval(A,B,fill="blue")
					if game[x][y] == 2:
						canvas.create_line(A,B,fill="blue",width=10)
						canvas.create_line(C,D,fill="red",width=10)

		def DetectWin():
			for i in [1,2]:
				for x in range(3):
					if game[x][0] == game[x][1] == game[x][2] == i : return i
				for y in range(3):
					if game[0][y] == game[1][y] == game[2][y] == i : return i
				if game[0][0] == game[1][1] == game[2][2] == i : return i
				if game[0][2] == game[1][1] == game[2][0] == i : return i
			return 0

		def SearchEmptyCases():
			L = []
			for x in range(3):
				for y in range(3):
					if game[x][y] == 0:
						L.append((x,y))
			if len(L) == 0 : return False 
			else :
				i = random.randint(0,len(L)-1)
				return L[i]

		#program
		def prog():
			gril()

		def affiche():
			canvas.delete("all")
			gril()
			pions()

		#click event
		def click(event):
			global game
			affiche()
			x = event.x // 100
			y = event.y // 100

			if DetectWin() != 0:
				game = [[0,0,0],[0,0,0],[0,0,0]]
				affiche()
				return

			if game[x][y] != 0 : return

		#human player 
			game[x][y] = 1 
			pions()
			if DetectWin() == 1:
				gril("blue")
				return

		#computer player 
			calcul = SearchEmptyCases()
			if calcul != False:
				x,y = calcul
				game[x][y] = 2
				pions()
				if DetectWin() == 2:
					gril("red")
					return

		#window
		window = Tk()
		window.title("Morpion By Gam's")
		window_size = 300
		window.geometry(str(window_size) + "x" + str(window_size))
		canvas = Canvas(window, width=window_size, height=window_size, borderwidth=0, highlightthickness=0, bg="lightgray")
		canvas.pack()
		window.after(100, prog)
		window.bind("<Button-1>", click)
		window.mainloop()


	if select == '1':
		Lounux()

	elif select == '2':
		chifoumi()

	elif select == '3':
		morpion()


def genpass():

	import random 
	import secrets

	init()

	print(Fore.BLUE + """          ________                 __________                         
	 /  _____/   ____    ____  \______   \_____     ______  ______
	/   \  ___ _/ __ \  /    \  |     ___/\__  \   /  ___/ /  ___/
	\     \_\  \\  ___/ |   |  \ |    |     / __ \_ \___ \  \___ \ 
	 \______  / \___  >|___|  / |____|    (____  //____  >/____  >
	        \/      \/      \/                 \/      \/      \/ 
                                                     By Gam's\n""")

	print(Fore.GREEN + "1- Mot de passe normal : 8 caractères , contenant lettres majuscules et minuscules avec chiffres\n2- Mot de passe sécurisé : Plus de 8 caractères contenant lettres majuscules et minuscules , avec chiffres et caractères spéciaux\n")
	level = input("Choisissez une option : ")

	def npass():
		chars = "abcdefghijklmnopqrsuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	
		password = ''
	
		for i in range(8):
			password = f"{password}{random.choice(chars)}"		

		print(f"Mot de passe : {password}")
	
		with open("password.txt", "a+") as file:
			file.write(f"Mot de passe : {password}\n")
			file.close()

		print("\nVotre mot de passe est stocké dans le fichier password.txt")

	def spass():
		chars = "abcdefghijklmnopqrsuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,?;.:/!§%#@"
	
		password = ''

		for i in range(16):
			password = f"{password}{random.choice(chars)}"		

		print(f"Mot de passe : {password}")
	
		with open("password.txt", "a+") as file:
			file.write(f"Mot de passe : {password}\n")
			file.close()

		print("\nVotre mot de passe est stocké dans le fichier password.txt")

	if level == '1':
		npass()

	if level == '2':
		spass()


def pycrypt():
	import time 
	from hashlib import sha256
	from pystyle import Anime, Colors, Colorate, Center, Box
	from colorama import Fore, Back, Style

	banner = """.______   ____    ____  ______ .______     ____    ____ .______   .___________.
|   _  \  \   \  /   / /      ||   _  \    \   \  /   / |   _  \  |           |
|  |_)  |  \   \/   / |  ,----'|  |_)  |    \   \/   /  |  |_)  | `---|  |----`
|   ___/    \_    _/  |  |     |      /      \_    _/   |   ___/      |  |     
|  |          |  |    |  `----.|  |\  \----.   |  |     |  |          |  |     
| _|          |__|     \______|| _| `._____|   |__|     | _|          |__|     
                                                                               """
	print((Center.XCenter(Box.DoubleCube(banner))))

	senetence_1 = (Fore.GREEN + "\nCe crypteur chiffre en XOR , assez efficace mais facile a décrypter si vous avez la clé")

	for char in senetence_1:
		time.sleep(0.1)
		print(char, end='', flush=True)

	entree = input("\nFichier a crypter : ")
	exit = input("Nom du fichier final : ")
	key = input("Entrez la clé : ")
	keys = sha256(key.encode('utf-8')).digest()

	with open(entree,'rb') as a_entree:
		with open(exit,'wb') as a_exit:
			i = 0
			while a_entree.peek():
				b = ord(a_entree.read(1))
				c = i % len(keys)
				d = bytes([c^keys[c]])
				a_exit.write(d)
				i = i + 1 

	sentence_2 = (Fore.GREEN + "Le fichier ",exit," a été crée sur votre repertoire actuel")

	for char in sentence_2:
		time.sleep(0.1)
		print(char, end='', flush=True)






if choice == '1':
	games()

if choice == '2':
	genpass()

if choice == '3':
	pycrypt()
