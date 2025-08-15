
print("\nBienvenu dans notre programme de la création du profit personnel")

print("S'il vous plait veuilez répondre aus questions suivantes pour créer votre profit ")

# Information personnel
nom = input("\nQuel est votre nom (Nom complet) ? \n Votre nom : ")
age = int(input("\nQuel est votre âge ? \nVotre âge : "))
situation = input("\nQuelle est votre situation matrimoniale ? \nVotre situation : ")

nationalite = input("\nQuel est votre nationalité ? \n Votre nationalité : ")

ville = input("\nVous vivez dans quelle ville actuellement ? \n Votre ville : ")

#Préférence
plat = input("\nQuel plat vous aimez manger ? \n Votre plat préférer : ")
couleur = input("\nQuelle est votre coleur préférer ? \n Votre couleur préférer : ")
musique = input("\nQuelle musique vous aimez danser ? \n Votre musique préférer : ")
sport = input("\nQuelle activité sportive voue aimez faire ? \n Votre activité sportive : ")

# Les projet
reve = input("\nDésolé mais quel est votre rêve ?\n Votre rêve : ")
objectif = input("\nQuelles sont vos objectifs pour cette année ?\n Vos objectifs : ")

# Affichage
print("==========================================")
print("+           Profi perso !                 +")
print("==========================================")

print("\nVos corodonnées :\n")
print("Nom : ", nom)
print("Age : ", age)
print("Situation matrimoniale : ", situation)
print("Nationalité : ", nationalite)
print("Ville actuelle : ", ville)

print("\nProjet et Ambitions\n")
print("Vous rêvez de devenir un(e)  ", reve)
print("Votre objectif cette année est de : ", objectif)

print("\nVos Préférences\n")
print("Plat : ", plat)
print("Couleur : ", couleur)
print("Musique : ", musique)
print("Sport : ", sport)
