from curses import qiflush
import pdb 

from models.artist import Artist
from models.print import Print

import repositories.artist_repository as artist_repository
import repositories.print_repository as print_repository 

artist_repository.delete_all()
print_repository.delete_all()

artist_1 = Artist("Nael Hanna")
artist_2 = Artist("George Birrell")
artist_3 = Artist("Shelagh Campbell")
artist_4 = Artist("Rebecca Collins")
artist_5 = Artist("Matthew Draper")
artist_6 = Artist("Barry McGlashan")
artist_7 = Artist("David Cook")
artist_8 = Artist("Deborah Phillips")

artist_repository.save(artist_1)
artist_repository.save(artist_2)
artist_repository.save(artist_3)
artist_repository.save(artist_4)
artist_repository.save(artist_5)
artist_repository.save(artist_6)
artist_repository.save(artist_7)
artist_repository.save(artist_8)

artists = artist_repository.select_all()

for artist in artists:
    print(artist.__dict__)

print_1 = Print("West Haven Waters Angus", artist_1, "25cm x 81cm", 35, 6, 500)
print_2 = Print("Fishing Boats and Creels", artist_1, "81cm x 81cm", 30, 6, 500)
print_3 = Print("Moonlight-Ethie, Scotland", artist_1, "81cm x 81cm", 30, 6, 500)
print_4 = Print("Smugglers Moon", artist_2, "50cm x 52cm", 35, 6, 400)
print_5 = Print("Early Morning Harbour", artist_2, "50cm x 52cm", 35, 6, 400)
print_6 = Print 

pdb.set_trace()