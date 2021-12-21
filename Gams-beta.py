import socket 
from datetime import *
from random import *
from colorama import*


print("""\n ██████╗  █████╗ ███╗   ███╗███████╗
██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██║  ███╗███████║██╔████╔██║███████╗
██║   ██║██╔══██║██║╚██╔╝██║╚════██║
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                       Beta by Gam's         """)

print("==========================================")

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

print("Your computer is : " + hostname, "\nYour computer IP adress is : " + IP)

time = date.today()
print("Date : ", time)

print("==========================================")

choice = input("WELCOME TO Gam's Tool !\n\nWhat do you want to start ?\n\n1 > I want to play a game\n\n2 > I want to generate a password\n")

def games():
	select = input("1 > Lounux By Gam's\n\n2 > Chifoumi By Gam's\n\nTapez ENTRER pour sortir")

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


	if select == '1':
		Lounux()

	elif select == '2':
		chifoumi()


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



if choice == '1':
	games()

if choice == '2':
	genpass()
