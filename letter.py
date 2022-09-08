class Letter:
    def __init__(self, title):
        self.title = title
        self.read = False

    def mark_as_read(self):
        self.read = True

    def return_read_status(self):
        return self.read
