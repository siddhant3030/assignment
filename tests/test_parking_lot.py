import unittest
import env
from bin import parking

class TestParkingLot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parking = parking.Parking()
        cls.allocated_slot = 1

def test_a_create_parking_lot(self):
        parking_slots = 6
        self.parking.create_parking_lot(parking_slots)
        self.assertEqual(len(self.parking.slots), parking_slots, msg="Wrong parking lot created")
