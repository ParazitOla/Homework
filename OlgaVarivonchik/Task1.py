### Task 6.1 Implement a Counter class which optionally accepts the start value and the counter stop value.
# If the start value is not specified the counter should begin with 0.
# If the stop value is not specified it should be counting up infinitely.
# If the counter reaches the stop value, print "Maximal value is reached." Implement to methods: "increment" and "get"
# * <em>If you are familiar with Exception rising use it to display the "Maximal value is reached." message.</em>

class Counter:

    def __init__(self, start=0, stop=None):

        self.start = start
        if stop == None:
            self.stop = start - 1
        else:
            self.stop = stop

    def increment(self):

        if (self.start < self.stop) or (self.start > self.stop):
            self.start += 1
        else:
            print("Maximal value is reached")

    def get(self):

        return print(self.start)


c = Counter(start=-4, stop=-1)
c.increment()
c.get()
c.increment()
c.get()
c.increment()
c.get()
c.increment()
c.get()
c.increment()
c.get()
