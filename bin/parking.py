import slot, car 

class Parking(object):

    def __init__(self):
        self.slots = {}

    def create_parking_lot(self, no_of_slots):
        no_of_slots = int(no_of_slots)

        if len(self.slots) > 0:
            print "Parking is already created"
            return

        if no_of_slots > 0:
            for i in range(1, no_of_slots+1):
                temp_slot = lot.PSlot(slot_no=i,
                                    available=True)
                self.slots[i] = temp_slot
            print "Created a parking lot with %s slots" % no_of_slots
        else:
            print "Number of slots provided is incorrect."
        return

    def get_nearest_available_slot(self):
        available_slots = filter(lambda x: x.available, self.slots.values())
        if not available_slots:
            return None
        return sorted(available_slots, key=lambda x: x.slot_no)[0]

    def park(self, reg_no, colour):
        if not self._do_primary_checks():
            return

        available_slot = self.get_nearest_available_slot()
        if available_slot:
            available_slot.car = car.Car.create(reg_no, colour)
            available_slot.available = False
            print "Allocated slot number: %s" % available_slot.slot_no
        else:
            print "Sorry, parking lot is full."
