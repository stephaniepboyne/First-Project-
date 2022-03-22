import pdb 

from models.artist import Artist
from models.print import Print

import repositories.artist_repository as artist_repository
import repositories.print_repository as print_repository 

print_repository.delete_all()
artist_repository.delete_all()


artist_1 = Artist("Nael Hanna", "http://www.thompsonsgallery.co.uk/artists-images/nael-hanna-fishing-boats-and-creels-mixed-media-32-x-32-inches-7500-unframed.jpg")
artist_2 = Artist("George Birrell", "https://cdn11.bigcommerce.com/s-cfdb8/images/stencil/1280x1280/products/185/263/East_Coast_Blues_4aa82fee205c2__96791.1297621555.jpg?c=2")
artist_3 = Artist("Rebecca Collins", "https://images.squarespace-cdn.com/content/v1/5c4a22dd29711455c39e8b20/1548366383322-FF96T3FNRWR6JS8LC309/1934_00613.jpg?format=2500w")
artist_4 = Artist("Matthew Draper", "https://scottishgallery.imgix.net/work/Cat.-26-Light-and-Air-2021-Pastel-on-paper-94cm-x-125cm-%C2%A377500.00-rfw.jpg?q=70&auto=compress,format&fit=clip&w=900&h=900")
artist_5 = Artist("Barry McGlashan", "https://scottishgallery.imgix.net/work/58.Islands-2021-oil-on-panel-30-x-40.5-cm.jpg?q=70&auto=compress,format&fit=clip&w=900&h=900")
artist_7 = Artist("Deborah Phillips", "http://www.strathearn-gallery.com/admin/images/items/FS_21243.JPG")

artist_repository.save(artist_1)
artist_repository.save(artist_2)
artist_repository.save(artist_3)
artist_repository.save(artist_4)
artist_repository.save(artist_5)
artist_repository.save(artist_7)

print_1 = Print("West Haven Waters, Angus", artist_1, "25cm x 81cm", 30, 20, 0, "http://www.thompsonsgallery.co.uk/artists-images/nael-hanna-2-unframed.jpg")
print_2 = Print("Fishing Boats and Creels", artist_1, "81cm x 81cm", 30, 20, 205, "http://www.thompsonsgallery.co.uk/artists-images/nael-hanna-fishing-boats-and-creels-mixed-media-32-x-32-inches-7500-unframed.jpg")
print_3 = Print("Moonlight over Angus", artist_1, "55cm x 70cm", 30, 20, 310, "http://www.thompsonsgallery.co.uk/artists-images/moonlightoverangusscotland.jpg")
print_4 = Print("East Coast Blues", artist_2, "50cm x 52cm", 40, 25, 190, "https://cdn11.bigcommerce.com/s-cfdb8/images/stencil/1280x1280/products/185/263/East_Coast_Blues_4aa82fee205c2__96791.1297621555.jpg?c=2")
print_5 = Print("Early Morning Harbour", artist_2, "50cm x 52cm", 40, 25, 200, "https://cdn11.bigcommerce.com/s-cfdb8/images/stencil/1280x1280/products/195/273/Early_Morning_Ha_4aa831c13f8ec__98198.1297621562.jpg?c=2")
print_6 = Print("Cannach", artist_3, "40cm x 60cm", 40, 25, 40, "https://images.squarespace-cdn.com/content/v1/5c4a22dd29711455c39e8b20/1548366383322-FF96T3FNRWR6JS8LC309/1934_00613.jpg?format=2500w")
print_7 = Print("Arnisdale", artist_3, "50cm x 40cm", 40, 25, 105, "https://images.squarespace-cdn.com/content/v1/5c4a22dd29711455c39e8b20/1548367189873-N984GJEHXWAS9L8IDLAZ/2007_Arnisdale.jpg?format=2500w") 
print_8 = Print("View of Five Sisters", artist_3, "70cm x 50xm", 40, 25, 95, "https://images.squarespace-cdn.com/content/v1/5c4a22dd29711455c39e8b20/1548366455955-KXYDPYRDDSJLS0LGDKJ9/1934_00631.jpg?format=2500w") 
print_9 = Print("Emerge From Rasaay to the Cuillin Hills", artist_4, "35cm x 55cm", 40, 25, 229, "https://scottishgallery.imgix.net/work/Cat.-23-Emerge-From-Raasay-to-the-Cuillin-Hills-2021-Pastel-on-paper-91cm-x156cm-%C2%A39250.00-rfw.jpg?q=70&auto=compress,format&fit=clip&w=900&h=900")
print_10 = Print("Light and Air", artist_4, "35cm x 55cm", 40, 25, 100, "https://scottishgallery.imgix.net/work/Cat.-26-Light-and-Air-2021-Pastel-on-paper-94cm-x-125cm-%C2%A377500.00-rfw.jpg?q=70&auto=compress,format&fit=clip&w=900&h=900")
print_17 = Print("Flowers", artist_5, "21cm x 60cm", 30, 20, 100, "https://scottishgallery.imgix.net/work/9.Flowers-2021-oil-paper-and-varnish-on-panel-30-x-21.5-cm.jpg?q=70&auto=compress,format&fit=clip&w=900&h=900")
print_11 = Print("Islands", artist_5, "30cm x 40cm", 30, 20, 109, "https://scottishgallery.imgix.net/work/58.Islands-2021-oil-on-panel-30-x-40.5-cm.jpg?q=70&auto=compress,format&fit=clip&w=900&h=900")
print_14 = Print("The Way through the Weeds", artist_7, "50cm x 50cm", 40, 25, 306, "http://www.strathearn-gallery.com/admin/images/cache/0-0-1-762-762/itemsfs_22599.JPG")
print_15 = Print("Cow Parsley Sunset", artist_7, "50cm x 45cm", 40, 25, 92, "http://www.strathearn-gallery.com/admin/images/items/FS_10506.JPG")
print_16 = Print("Twilight Flock and Rusty Barns", artist_7, "50cm x 45cm", 40, 25, 222, "http://www.strathearn-gallery.com/admin/images/items/FS_21243.JPG")

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
print_repository.save(print_17)
print_repository.save(print_14)
print_repository.save(print_15)
print_repository.save(print_16)

pdb.set_trace()