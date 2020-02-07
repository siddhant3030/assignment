import unittest
from Utilities import create_parking_lot, park_car, parking_lot_is_full, car_departure, \
    car_by_colour, slot_by_car_number, slot_by_colour


class TestParkingLotUtilities(unittest.TestCase):
    """
    will test the endpoints
    """

    def test_create_parking_lot(self):
        testParkingLot = create_parking_lot(str(6))
        self.assertEqual(len(testParkingLot.get_slots()), 6)

    
    #if the parking lot is full
    def test_parking_lot_is_full(self):
        testParkingLot = create_parking_lot(str(6))
        self.assertEqual(parking_lot_is_full(testParkingLot), False)


if __name__ == '__main__':
    unittest.main()
