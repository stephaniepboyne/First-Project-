import unittest
from models.artist import Artist 

class TestArtist(unittest.TestCase):

    def setUp(self):
        self.artist = Artist("Nael Hanna", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Monet_-_Impression%2C_Sunrise.jpg/800px-Monet_-_Impression%2C_Sunrise.jpg", id=None)
    
    def test_artist_has_name(self):
        self.assertEqual("Nael Hanna", self.artist.name)

    def test_artist_has_pathway(self):
        self.assertEqual("https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Monet_-_Impression%2C_Sunrise.jpg/800px-Monet_-_Impression%2C_Sunrise.jpg", self.artist.image_pathway)
