pcode = input("Ingrese su código postal: ")
longitud = len(pcode)
lt01 = pcode[0].upper()
lt02 = pcode[1].upper()
npcode = lt01+lt02+pcode[2:longitud]
print("La código se guardara como:",npcode)