import csv

file = open("Books.csv","w")
newRecord ="To Kill a Mockingbird,Harper Lee,1960\n"
file.write(str(newRecord))
newRecord ="A brief History of Time,Stephen Hawking,1988\n"
file.write(str(newRecord))
newRecord ="The Great Gatsby,F. Scott Fitzgerald,1922\n"
file.write(str(newRecord))
newRecord ="The Man Who Mistook His Wife for a Hat,Oliver Snacks,1985\n"
file.write(str(newRecord))
newRecord ="Pride and Prejudice,Jane Austen,1813\n"
file.write(str(newRecord))
newRecord ="Cabal,Clive Barker,1994\n"
file.write(str(newRecord))
newRecord ="Drácula,Jane Bram Stoker,1897\n"
file.write(str(newRecord))
newRecord ="Frankesnstein o el moderno Prometeo,Mary Shelley,1823\n"
file.write(str(newRecord))
newRecord ="It,Stephen King,1986\n"
file.write(str(newRecord))
newRecord ="Otra vuelta de tuerca,Henry James,1898\n"
file.write(str(newRecord))
newRecord ="En las montañas de la locura,H. P. Lovecraft,1936\n"
file.write(str(newRecord))
file.close()