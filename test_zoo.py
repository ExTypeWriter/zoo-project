import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        # C1b2: 0 <= age <= 12
        self.assertEqual(self.zoo.get_ticket_price(0), 50)  
        self.assertEqual(self.zoo.get_ticket_price(6), 50) 
        self.assertEqual(self.zoo.get_ticket_price(12), 50) 

    def test_teenage_ticket_price(self):
        # C1b3: 13 <= age <= 20
        self.assertEqual(self.zoo.get_ticket_price(13), 100)  
        self.assertEqual(self.zoo.get_ticket_price(16), 100)  
        self.assertEqual(self.zoo.get_ticket_price(20), 100)  

    def test_adult_ticket_price(self):
        # C1b4: 21 <= age <= 60
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
        self.assertEqual(self.zoo.get_ticket_price(40), 150)
        self.assertEqual(self.zoo.get_ticket_price(60), 150)  

    def test_elder_ticket_price(self):
        # C1b6: age > 60
        self.assertEqual(self.zoo.get_ticket_price(61), 100)  # Boundary
        self.assertEqual(self.zoo.get_ticket_price(75), 100)  # Middle value
        self.assertEqual(self.zoo.get_ticket_price(90), 100)  # Representative value

    def test_invalid_age(self):
        # C1b1: age < 0
        with self.assertRaises(ValueError):
            self.zoo.get_ticket_price(-1)
        with self.assertRaises(ValueError):
            self.zoo.get_ticket_price(-10)

if __name__ == '__main__':
    unittest.main()