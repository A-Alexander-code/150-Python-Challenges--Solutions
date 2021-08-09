signatures = ["math","science","chemistry","phisyc","literature","history"]

for i in signatures:
    print(i)

qst = input("¿Cuál de las anteriores asignaturas no era su preferida? ")
qst = qst.lower()

getrid = signatures.index(qst)
del signatures[getrid]

print(signatures)