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

    #if car is not defined
    def test_park_car_lot_not_defined(self):
        testString = park_car(None, 'KA-01-AA-1111', 'White')
        self.assertEqual('Parking lot is not defined', testString)
    
    #more tests on car 
    def test_park_car_lot_allocated(self):
        testParkingLot = create_parking_lot(str(6))
        testString = park_car(testParkingLot, 'KA-01-AA-1112', 'White')
        self.assertEqual('Allocated slot number: 1', testString)

    def test_park_car_lot_full(self):
        testParkingLot = create_parking_lot(str(1))
        testParkString = park_car(testParkingLot, 'KA-01-AA-1112', 'White')
        testString = park_car(testParkingLot, 'KA-01-AA-1113', 'White')
        self.assertEqual('Sorry, parking lot is full', testString)

    def test_car_by_colour(self):
        testParkingLot = create_parking_lot(str(6))
        testParkString = park_car(testParkingLot, 'KA-01-AA-1117', 'White')
        testString = car_by_colour(testParkingLot, 'White')
        self.assertEqual(testString, 'KA-01-AA-1117, ')


if __name__ == '__main__':
    unittest.main()
