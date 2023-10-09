note1 = float(input("Entrez la première note : "))
note2 = float(input("Entrez la deuxième note : "))
note3 = float(input("Entrez la troisième note : "))

moyenne = (note1 + note2 + note3) / 3

print("La moyenne de l'étudiant est :", moyenne)

if moyenne >= 16:
    print("Mention : Très bien")
elif moyenne >= 14 and moyenne < 16:
    print("Mention : Bien")
elif moyenne >= 12 and moyenne < 14:
    print("Mention : Assez bien")
elif moyenne >= 10 and moyenne < 12:
    print("Mention : Passable")
else:
    print("Mention : Insuffisant")
