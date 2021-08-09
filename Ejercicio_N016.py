print("Responda las sigguientes preguntas con 'si' o 'no'")
resp1 = input("¿Está lloviendo?\n")
resp1 = str.lower(resp1)
if resp1 =="si":
    resp2 = input("¿El viento es fuerte?\n")
    resp2 = str.lower(resp2)
    if resp2 == "si":
        print("Hace mucho viento para usar sombrilla")
    else:
        print("Toma una sombrilla")
else:
    print("¡Disfruta de tu día!")
