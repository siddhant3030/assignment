import unittest
import env
from bin import parking

class TestParkingLot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parking = parking.Parking()
        cls.allocated_slot = 1