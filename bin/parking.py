import slot, car 

class Parking(object):

    def __init__(self):
        self.slots = {}

    def create_parking_lot(self, no_of_slots):
        no_of_slots = int(no_of_slots)

        if len(self.slots) > 0:
            print "Parking Lot already created"
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
