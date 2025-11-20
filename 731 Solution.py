class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        active = [(startTime, endTime)]
        new_ind = 0
        for i,(bookStart, bookEnd) in enumerate(self.bookings):
            if endTime <= bookEnd:
                new_ind = i + 1
            if bookStart >= endTime:
                continue
            if bookEnd < startTime:
                break
            active = list(filter(lambda x: x[0] < bookEnd, active))
            active.append((bookStart,bookEnd))
            if len(active) >= 3:
                return False

        self.bookings.insert(new_ind, (startTime, endTime))
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
