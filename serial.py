class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=100):
        self.start = start
        self.default = start

    def generate(self):
        self.start += 1
        return self.start - 1

    def reset(self):
        self.start = self.default

    def __repr__(self):
        return f"<SerialGenerator start={self.start} default={self.default}>"
