class Letter:
    def __init__(self, content):
        """
        Letter object that contains a content string.
        
        :param content: string
        """
        self.content = content
        self.read = False

    def mark_as_read(self):
        """
        Sets read to True.
        """
        self.read = True

    def return_read_status(self):
        """
        Returns bool of the read status of the letter.

        :return: bool
        """
        return self.read
