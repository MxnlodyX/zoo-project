import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()
    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
        
    def test_invalid_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-10), "Invalid")
    def test_second_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(8), 50)
    def test_student_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(18), 100)
    def test_people_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(35), 150)
    def test_elderly_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(64), 100)

if __name__ == '__main__':
    unittest.main()