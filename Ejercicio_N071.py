sport = ["soccer","football"]
qst = input("¿Cuál es su deporte favorito?\n")
qst = qst.lower()
sport.append(qst)
sport.sort()
print(sport)