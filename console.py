import pdb 

from models.artist import Artist
from models.print import Print

import repositories.artist_repository as artist_repository
import repositories.print_repository as print_repository 

print_repository.delete_all()
artist_repository.delete_all()


artist_1 = Artist("Nael Hanna")
artist_2 = Artist("George Birrell")
artist_3 = Artist("Rebecca Collins")
artist_4 = Artist("Matthew Draper")
artist_5 = Artist("Barry McGlashan")
artist_6 = Artist("David Cook")
artist_7 = Artist("Deborah Phillips")

artist_repository.save(artist_1)
artist_repository.save(artist_2)
artist_repository.save(artist_3)
artist_repository.save(artist_4)
artist_repository.save(artist_5)
artist_repository.save(artist_6)
artist_repository.save(artist_7)

print_1 = Print("West Haven Waters Angus", artist_1, "25cm x 81cm", 30, 20, 200)
print_2 = Print("Fishing Boats and Creels", artist_1, "81cm x 81cm", 30, 20, 205)
print_3 = Print("Moonlight-Ethie, Scotland", artist_1, "81cm x 81cm", 30, 20, 310)
print_4 = Print("Smugglers Moon", artist_2, "50cm x 52cm", 40, 25, 190)
print_5 = Print("Early Morning Harbour", artist_2, "50cm x 52cm", 40, 25, 200)
print_6 = Print("Cannach", artist_3, "40cm x 60cm", 40, 25, 40)
print_7 = Print("Arnisdale", artist_3, "50cm x 40cm", 40, 25, 105) 
print_8 = Print("View of Five Sisters", artist_3, "70cm x 50xm", 40, 25, 95) 
print_9 = Print("Emerge From Rasaay to the Cuillin Hills", artist_4, "35cm x 55cm", 40, 25, 229)
print_10 = Print("Light and Air", artist_4, "35cm x 55cm", 40, 25, 100)
print_11 = Print("Islands", artist_5, "30cm x 40cm", 30, 20, 109)
print_12 = Print("February IV", artist_6, "30cm x 25cm", 30, 20, 205)
print_13 = Print ("Flower Study IV", artist_6, "22cm x 20cm", 30, 20, 102)
print_14 = Print("The Way through the Weeds", artist_7, "50cm x 50cm", 40, 25, 306)
print_15 = Print("Cow Parsley Sunset", artist_7, "50cm x 45cm", 40, 25, 92)
print_16 = Print("Twilight Flock and Rusty Barns", artist_7, "50cm x 45cm", 40, 25, 222)

print_repository.save(print_1)
print_repository.save(print_2)
print_repository.save(print_3)
print_repository.save(print_4)
print_repository.save(print_5)
print_repository.save(print_6)
print_repository.save(print_7)
print_repository.save(print_8)
print_repository.save(print_9)
print_repository.save(print_10)
print_repository.save(print_11)
print_repository.save(print_12)
print_repository.save(print_13)
print_repository.save(print_14)
print_repository.save(print_15)
print_repository.save(print_16)

pdb.set_trace()