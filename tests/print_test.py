import unittest
from models.print import Print 

class TestPrint(unittest.TestCase):

    def setUp(self):
        self.print = Print("West Haven Waters, Angus", "Nael Hanna", "25cm x 81cm", 30, 20, 0, "http://www.thompsonsgallery.co.uk/artists-images/nael-hanna-2-unframed.jpg", id=None)
    
    def test_print_has_artist(self):
        self.assertEqual("Nael Hanna", self.print.artist)
    
    def test_print_has_size(self):
        self.assertEqual("25cm x 81cm", self.print.size)
    
    def test_print_has_price(self):
        self.assertEqual(30, self.print.price)
    
    def test_print_has_printing_cost(self):
        self.assertEqual(20, self.print.printing_cost)
    
    def test_print_has_stock(self):
        self.assertEqual(0, self.print.stock)

    def test_print_has_title(self):
        self.assertEqual("West Haven Waters, Angus", self.print.title)

    def test_print_has_pathway(self):
        self.assertEqual("http://www.thompsonsgallery.co.uk/artists-images/nael-hanna-2-unframed.jpg", self.print.image_print_pathway)
