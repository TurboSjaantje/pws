import random
naam = input("Naam van het bestand:  ")
aantal = input("Hoeveel rijen?    ")

file = open(r"{}.txt".format(naam),"w+")

zin = ""

for x in range(0, int(aantal)):
    ranlong = random.randrange(818735, 831712)
    ranlat = random.randrange(734792, 803951) 
    lengtegraad = "51.{}".format(ranlong)
    breedtegraad = "4.{}".format(ranlat)

    ranjaar = random.randrange(2019, 2021)
    ranmaand = random.randrange(1, 13)
    randag = random.randrange(1, 30)

    ranjaar1 = random.randrange(ranjaar, 2021)
    ranmaand1 = random.randrange(ranmaand, 13)
    randag1 = random.randrange(randag, 30)
    
    datum_plaatsing = "{}-{}-{}".format(ranjaar, ranmaand, randag)
    datum_batterij = "{}-{}-{}".format(ranjaar1, ranmaand1, randag1)

    nieuw = '("{}", "{}", "{}", "{}"), '.format(str(lengtegraad), str(breedtegraad), str(datum_plaatsing), str(datum_batterij))

    if(x == int(aantal)-1):
        nieuw = nieuw[:-2]
    
    zin += nieuw



file.write("INSERT INTO `Prullenbak`(`lengtegraad`, `breedtegraad`, `datum_plaatsing`, `datum_batterij`) VALUES " + zin)

file.close()

