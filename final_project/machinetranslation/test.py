import unittest

from translator import french_to_english, english_to_french
        
class test_english_to_french(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertNotEqual(english_to_french(None),"Bonjour")

class test_french_to_english(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertNotEqual(french_to_english(None),"Hello")

unittest.main()