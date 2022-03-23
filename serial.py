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
        """Create serial with start varable and set default to the start"""
        self.start = start
        self.default = start

    def generate(self):
        """Adds one to start and returns start minus one"""
        self.start += 1
        return self.start - 1

    def reset(self):
        """Sets start back to default value"""
        self.start = self.default

    def __repr__(self):
        """Documenting Instance"""
        return f"<SerialGenerator start={self.start} default={self.default}>"
