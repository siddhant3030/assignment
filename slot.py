class PSlot(object):

    def __init__(self, slot_no=None, available=None):
        self.car = None
        self.slot_no = slot_no
        self.available = available
    
    @property
    def car(self):
        return self._car

    @car.setter
    def car(self, value):
        self._car = value
