print("\n\n================================================")
print("|| Vérificateur d'éligibilité du tranche UL    ||")
print("=================================================\n\n")
print("Veuillez répondre les question suivantes pour vérifier votre éligibilité. \n")

age = int(input("Quel est votre âga ?\nVotre Age : "))

MentionBac = input("quelle est votre mention au BAC ?\nVotre mention  :")
insciption = input("Vous êtes déja inscrit à l'UL ?(oui ou non) \nEtat de votre inscription : ")
nationalite = input("Quelle est votre nationalité ?\nVotre nationalité : ")

# Vérification
VerifiAge = age <= 22
VerifiMention =(MentionBac in ("BIEN", "Bien", "bien") or MentionBac in ("Très Bien","Très BIEN","Très bien"))
VerifieInscription = insciption in ("OUI","Oui","oui" )
VerifieNationalite = nationalite in ("Togolaise", "togolaise", "TOGOLAISE")

# Affichage du résultat
print("\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
print("+    Résultats des vérifications     +")
print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n\n")
print(f"Âge ≤ 22 ans : {VerifiAge }")
print(f"Mention (Bien ou Très Bien) : {VerifiMention}")
print(f"Inscription UL : { VerifieInscription}")
print(f"Nationalité togolaise : {VerifieNationalite}")
elibibileGenerale = VerifiAge and VerifieNationalite and VerifieInscription and VerifiMention
print(f"Éligibilité générale (tous critères vrais) : {elibibileGenerale}")