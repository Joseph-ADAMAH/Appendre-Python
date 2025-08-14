print("Calculateur d'éonomie version Groupe A2")
nom = input("Vueillez entrer votre nom : ")

revenuMensuel = int(input("Quel est votre revenu mensuel(en FCFA) ? : "))
depense = int(input("Quel est votre dépense mensuel ? (en FCFA) : "))

economie = revenuMensuel - depense
taux  = (economie/revenuMensuel)*100

print("\n°°°°°°°°°Bilan mensuel°°°°°°°°°\n")
print("Nom : ", nom)
print("Revenu", revenuMensuel,"FCFA")
print("Dépense :", depense,"FCFA")
print("Taux d'épargne : ", taux,"%")