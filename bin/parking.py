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

    def leave(self, slot_no):
        slot_no = int(slot_no)
        if not self._do_primary_checks():
            return

        if slot_no in self.slots:
            pslot = self.slots[slot_no]
            if not pslot.available and pslot.car:
                pslot.car = None
                pslot.available = True
                print "Slot number %s is free" % slot_no
            else:
                print "No car is present at slot number %s" % slot_no
        else:
            print "Sorry, slot number does not exist in parking lot."

    def status(self):
        """Method to show current status of parking
        """

        if not self._do_primary_checks():
            return

        print "Slot No\tRegistration No\tColour"
        for i in self.slots.values():
            if not i.available and i.car:
                print "%s\t%s\t%s" % (i.slot_no, i.car.reg_no, i.car.colour)

    def _do_primary_checks(self):
        if len(self.slots) == 0:
            print "Parking Lot not created"
            return False
        return True

    