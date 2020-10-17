import random
naam = input("Naam van het bestand:  ")
aantal = input("Hoeveel prullenbakken?    ")

file = open(r"{}.txt".format(naam),"w+")

zin = ""

for x in range(11, int(aantal)+11):

    prullenbak_id = x
    meting_type1 = random.randrange(8, 70)

    nieuw = '("{}", "{}"), '.format(str(prullenbak_id), str(meting_type1))

    if(x == int(aantal)+11-1):
        nieuw = nieuw[:-2]
    
    zin += nieuw

file.write("INSERT INTO `Data`(`prullenbak_id`, `meting_type1`) VALUES " + zin)

file.close()
